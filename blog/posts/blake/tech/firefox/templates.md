<!--
.. title: ES6 Templates
.. date: 2015-01-12 14:45
.. author: Blake Winton
.. tags: mozilla, templates, es6
-->

One of my favourite upcoming features in ES6 is Template Strings.  I’ve used
JQuery’s [templates](http://ejohn.org/blog/javascript-micro-templating/) in
[some previous code](https://bugzilla.mozilla.org/show_bug.cgi?id=686347) I’ve
worked on, and while it was very useful in finishing the feature on time, it’s
aged now and relying on third-party libraries which we don’t have time to keep
up to date isn’t the best idea and so we’re in the middle of [some work to
remove them](https://bugzilla.mozilla.org/show_bug.cgi?id=1014609).  So having
said that, I’m quite happy to see something similar arriving in the base
language, so that we can take advantage of it without having to add any extra
code.

> As an aside, all the code below was tested in [Firefox
> 34](http://getfirefox.com), using the
> [Scratchpad](https://developer.mozilla.org/en-US/docs/Tools/Scratchpad).  The
> comments are pasted in below the code when you select it and choose the
> `Execute » Display` menu item or hit `Ctrl+L` (`Cmd+L` on Mac).  I
> [hear](https://twitter.com/addyosmani/status/541978036904554496) they also
> [work in Chrome](https://plus.google.com/+AddyOsmani/posts/BW5h61SoGf8), but
> they didn’t seem to in the version I was running (39.0.2171.95), and I didn’t
> want to start messing with an `--es-staging` flag.  If someone can confirm
> whether they work or not, I would certainly appreciate it!  :)

<!-- TEASER_END -->

At their simplest, template strings are just like regular strings, only with
backticks (`` ` ``) instead of single (`'`) or double (`"`) quotes.
```js
function test0() {
  return `Just a normal-ish string.`
}

test0();

/*
Just a normal-ish string.
*/
```

but if that were all they were, they wouldn’t be very useful, so obviously they
can do more.  And the first extra thing they can do is capture the values of
variables from the scope they’re defined in, and insert them into the string,
like so:
```js
function test1() {
  let x = 1;
  let y = 'foo';

  return `x is ${x}, and y is ${y}.`
}

test1();

/*
x is 1, and y is foo.
*/
```

Now, you may say “But Blake, I could have just put the values right in the
string myself!”.  Well, in this case yes, you could, but those values don’t have
to be statically defined in the function they’re used from…
```js
function test2(x, y) {
  return `x is ${x}, and y is ${y}.`
}

test2(1, 'foo');

/*
x is 1, and y is foo.
*/
```

I’m sure you can imagine the values coming from the result of an XHR call, or
some other asynchronous function.  But just to hammer the point home even
further, the variables themselves don’t need to be in the function at all…
```js
function test3(x) {
  return function (y) {
    return `x is ${x}, and y is ${y}, and the sum is ${x + y}.`
  }
}

let partial = test3(1);
partial(2);

/*
x is 1, and y is 2, and the sum is 3.
*/
```
Notice that we can also evaluate expressions in the template string.  That would
be much harder to do with hard-coded values.

[But wait, there’s more!](https://www.youtube.com/watch?v=ZTpXh33Mbeg)

It turns out we have control not only over what we inject into the string, but
also what comes out of the injected string!  If we put the name of a function
before the backtick, then it will get called when the string is created, and it
can return *whatever* it wants.  Like, really, **_whatever_**!  :)

```js
function test4() {
  function replace(template, arg) {
    return new Date(arg);
  }
  let x = "2014-12-27T04:09:57.054Z";

  return replace`This doesn’t matter we only use ${x} here.`.getUTCDate();
}

test4();

/*
27
*/
```

Have you ever called `.getUTCDate()` on a string before?  Me either!  Of course,
you’re not limited to dates.  You could also return a model object that was
populated from various pieces of data you passed in, if you felt like rolling
framework-style.  For the rest of the examples, I think I’ll stick to returning
strings, though, since more complicated structures just show up as `[object]`,
which isn’t so helpful for demonstrating stuff.

So, let’s see just what gets passed in to this function…
```js
function test5() {
  function modify(template, ...args) {
    return 'Nope!\n  template=' + JSON.stringify(template) +
      '\n  args=' + JSON.stringify(args);
  }
  let x = 1;
  let y = 3;

  return modify`x is ${x}, and y is ${y}, and the sum is ${x + y}.`;
}

test5();

/*
Nope!
  template=["x is ",", and y is ",", and the sum is ","."]
  args=[1,3,4]
*/
```

Well, that’s not so terrible.  The template string is broken up into the pieces
between the arguments, and the arguments are pre-calculated before being passed
in.  Hmm, I wonder what happens if you have two expressions right beside each
other?
```js
function test6() {
  function modify(template, ...args) {
    return 'Nope!\n  template=' + JSON.stringify(template) +
      '\n  args=' + JSON.stringify(args);
  }
  let x = 1;
  let y = 'foo';

  return modify`Adjacent items give: ${x}${y}.`;
}

test6();

/*
Nope!
  template=["Adjacent items give: ","","."]
  args=[1,"foo"]
*/
```

You get an empty string.  Seems reasonable.  Now, if you want to put the string
back together, you’ll need to loop over each item in the template, and append
the expression in the same position (if it exists!  If the template string ends
with static content, then there will be no last expression).  Of course, while
you’re doing that, you can process the arguments in any way you see fit, like,
say, selectively escaping unsafe HTML characters…

```js
function test7() {
  function escape(data) {
    return data.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function html(template, ...args) {
    let retval = '';
    for (let i in template) {
      retval += template[i] + (args[i] ? escape(args[i]) : '');
    }
    return retval;
  }
  let x = 'my & name';
  let y = '<script><!--';

  return html`<span>x is ${x}</span>, and <span>y is ${y}</span>.`;
}

test7();

/*
<span>x is my &amp; name</span>, and <span>y is &lt;script&gt;&lt;!--</span>.
*/
```

Or better yet, automatically translating your strings into another language!
```js
function test8() {
  locale = {
    'my first string' : function (args) {
      return 'mi primera cadena';
    },
    'My name is |, and I like |.' : function (args) {
      retval = '';
      translated = 'Mi nombre es |, y me gusta |.'.split('|');
      for (let i in translated) {
        retval += translated[i] + (args[i] || '');
      }

      return retval;
    }
  }
  function _(template, ...args) {
    return locale[template.join('|')](args);
  }
  let x = 'Blake';
  let y = 'JavaScript';

  return _`My name is ${x}, and I like ${y}.`;
}

test8();

/*
Mi nombre es Blake, y me gusta JavaScript.
*/
```

(We have to pretend that the `locale` dictionary gets loaded from a more
complicated sub-system, and yes, this totally fails to handle languages with a
different word order, but I trust you get the idea behind it, and I can leave
the hard work of actually implementing it to the reader.)

Hopefully this brief set of examples has piqued your curiousity.  If you’ld like
to read some more technical infomation about template strings, you should check
out [this wiki page](http://tc39wiki.calculist.org/es6/template-strings/)…
