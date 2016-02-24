<!--
.. title: Hey!  Let’s Write a WebExtension!
.. date: 2015-09-21 14:52
.. author: Blake Winton
.. tags: webextension, firefox, addon, mozilla
-->

<small>(This article is also posted on [Mozilla
Hacks](https://hacks.mozilla.org/2015/09/lets_write_a_webextension/).)</small>

You might have heard about Mozilla’s [WebExtensions][1ec53d8c], our
implementation of a new browser extension API for writing
multiprocess-compatible add-ons.  Maybe you’ve been wondering what it was about,
and how you could use it. Well, I’m here to help!  I think [MDN’s WebExtensions
Docs][0fae7804] have a pretty great definition:

> WebExtensions are a new way to write Firefox extensions.
>
> The technology is developed for cross-browser compatibility: to a large extent
> the API is compatible with the [extension API][f2b3806b] supported by Google
> Chrome and Opera. Extensions written for these browsers will in most cases run
> in Firefox with just a few changes. The API is also fully compatible with
> [multiprocess Firefox][98536158].

The only thing I would add is that while Mozilla is implementing most of the API
that Chrome and Opera support, we’re not restricting ourselves to only that API.
Where it makes sense, we will be adding new functionality and talking with other
browser makers about implementing it as well.  Finally, since the WebExtension
API is still under development, it’s probably best if you use [Firefox
Nightly][4f9d6081] for this tutorial, so that you get the most up-to-date,
standards-compliant behaviour.  But keep in mind, this is still experimental
technology — things might break!

### Starting off

Okay, let’s start with a reasonably simple add-on. We’ll add a button, and when
you click it, it will open up [one of my favourite sites][788ee3ee] in a new
tab.

<!-- TEASER_END -->

The first file we’ll need is a [`manifest.json`][4063d915], to tell Firefox
about our add-on.

```json
{
  "manifest_version": 2,
  "name": "Cat Gifs!",
  "version": "1.0",
  "applications": {
    "gecko": {
      "id": "catgifs@mozilla.org"
    }
  },

  "browser_action": {
    "default_title": "Cat Gifs!"
  }
}
```

Great!  We’re done!  Hopefully your code looks a little [like this][d61ba671].
Of course, we have no idea if it works yet, so let’s install it in Firefox
(we’re using Firefox Nightly for the latest implementation). You could try to
drag the `manifest.json`, or the whole directory, onto Firefox, but that really
won’t give you what you want.

[![The directory listing.](/images/blake/WebExtensions/HowTo/1-DirectoryListing.png)](/images/blake/WebExtensions/HowTo/large/1-DirectoryListing.png)

### Installing

To make Firefox recognize your extension as an add-on, you need to give it a zip
file which ends in `.xpi`, so let’s make one of those by first installing
[7-Zip][0f904c1a], and then typing `7z a catgifs.xpi manifest.json`. (If you’re
on Mac or Linux, the `zip` command should be built-in, so just type `zip
catgifs.xpi manifest.json`.) Then you can drag the `catgifs.xpi` onto Firefox,
and it will show you an error because our extension is unsigned.

[![The first error.](/images/blake/WebExtensions/HowTo/2-FirstError.png)](/images/blake/WebExtensions/HowTo/large/2-FirstError.png)

We can work around this by going to `about:config`, typing
`xpinstall.signatures.required` in the search box, double-clicking the entry to
set it to false, and then closing that tab.  After that, when we drop
`catgifs.xpi` onto Firefox, we get the option to install our new add-on!

> It’s important to note that as of Firefox 44 (later this year), add-ons will
[require a signature][533ab63e] to be installed on Firefox Beta or Release
versions of the brower, so even if you set the preference described above, you
will soon still need to be running Firefox Nightly or Developer Edition to
follow this tutorial.

[![Success!!!](/images/blake/WebExtensions/HowTo/3-SuccessDialog.png)](/images/blake/WebExtensions/HowTo/large/3-SuccessDialog.png)

Of course, our add-on doesn’t do a whole lot yet.

[![I click and click, but nothing happens.](/images/blake/WebExtensions/HowTo/4-ButtonClick.png)](/images/blake/WebExtensions/HowTo/large/4-ButtonClick.png)

So let’s fix that!

### Adding features

First, we’ll add the following lines to `manifest.json`, above the line
containing [`browser_action`][7e996c37]:

```json
  "background": {
    "scripts": ["background.js"],
    "persistent": false
  },
```

now, of course, that’s pointing at a `background.js` file that doesn’t exist
yet, so we should create that, too.  Let’s paste the following javascript in it:

```javascript
'use strict';

/*global chrome:false */

chrome.browserAction.setBadgeText({text: '(ツ)'});
chrome.browserAction.setBadgeBackgroundColor({color: '#eae'});

chrome.browserAction.onClicked.addListener(function(aTab) {
  chrome.tabs.create({'url': 'http://chilloutandwatchsomecatgifs.com/', 'active': true});
});
```

And you should get something that looks [like this][9582f75d].  Re-create the
add-on by typing `7z a catgifs.xpi manifest.json background.js` (or `zip
catgifs.xpi manifest.json background.js`), and drop `catgifs.xpi` onto Firefox
again, and now, when we click the button, we should get a new tab!  😄

![Cat Gifs!](/images/blake/WebExtensions/HowTo/5-CatGifs.gif)

### Automating the build

I don’t know about you, but I ended up typing `7z a catgifs.xpi manifest.json` a
disappointing number of times, and wondering why my `background.js` file wasn’t
running.  Since I know where this blog post is ending up, I know we’re going to
be adding a bunch more files, so I think it’s time to add a build script.  I
hear that the go-to build tool these days is [`gulp`][0686b7bc], so I’ll wait
here while you [go install that][157f3c41], and c’mon back when you’re done.  (I
needed to install [Node][2fc43570], and then gulp twice.  I’m not sure why.)

So now that we have gulp installed, we should make a file named `gulpfile.js` to
tell it how to build our add-on.

```javascript
'use strict';

var gulp = require('gulp');

var files = ['manifest.json', 'background.js'];
var xpiName = 'catgifs.xpi';

gulp.task('default', function () {
  console.log(files, xpiName)
});
```

Once you have that file looking something [like this][cb58b4da], you can type
`gulp`, and see output that looks something like this

[![Just some command line stuff, nbd.](/images/blake/WebExtensions/HowTo/6-GulpOutput.png)](/images/blake/WebExtensions/HowTo/large/6-GulpOutput.png)

Now, you may notice that we didn’t actually build the add-on.  To do that, we
will need to install another package to zip things up.  So, type `npm install
gulp-zip`, and then change the `gulpfile.js` to contain the following:

```javascript
'use strict';

var gulp = require('gulp');
var zip = require('gulp-zip');

var files = ['manifest.json', 'background.js'];
var xpiName = 'catgifs.xpi';

gulp.task('default', function () {
  gulp.src(files)
    .pipe(zip(xpiName))
    .pipe(gulp.dest('.'));
});
```

Once your `gulpfile.js` looks [like this][a6089ff2], when we run it, it will
create the `catgifs.xpi` (as we can tell by looking at the timestamp, or by
deleting it and seeing it get re-created).

### Fixing a bug

Now, if you’re like me, you clicked the button a whole bunch of times, to test
it out and make sure it’s working, and you might have ended up with a lot of
tabs.  While this will ensure you remain extra-chill, it would probably be nicer
to only have one tab, either creating it, or switching to it if it exists, when
we click the button.  So let’s go ahead and add that.

![Lots and lots of cats.](/images/blake/WebExtensions/HowTo/7-ManyTabbys.gif)

The first thing we want to do is see if the tab exists, so let’s edit the
`browserAction.onClicked` listener in `background.js` to contain the following:

```javascript
chrome.browserAction.onClicked.addListener(function(aTab) {
  chrome.tabs.query({'url': 'http://chilloutandwatchsomecatgifs.com/'}, (tabs) => {
    if (tabs.length === 0) {
      // There is no catgif tab!
      chrome.tabs.create({'url': 'http://chilloutandwatchsomecatgifs.com/', 'active': true});
    } else {
      // Do something here…
    }
  });
});
```

Huh, that’s weird, it’s always creating a new tab, no matter how many catgifs
tabs there are already…  It turns out that our add-on doesn’t have permission to
see the urls for existing tabs yet which is why it can’t find them, so let’s go
ahead and add that by inserting the following code above the `browser_action`:

```json
  "permissions": [
    "tabs"
  ],
```

and once your code looks [similar to this][4b287c05], re-run `gulp` to rebuild
the add-on, and drag-and-drop to install it, and then when we test it out,
ta-da!  Only one catgif tab!  Of course, if we’re on another tab it doesn’t do
anything, so let’s fix that.  We can change the `else` block to contain the
following:

```javascript
      // Do something here…
      chrome.tabs.query({'url': 'http://chilloutandwatchsomecatgifs.com/', 'active': true}, (active) => {
        if (active.length === 0) {
          chrome.tabs.update(tabs[0].id, {'active': true});
        }
      });
```

make sure it looks [like this][576c5422], rebuild, re-install, and shazam, it
works!

### Making it look nice

Well, it works, but it’s not really pretty.  Let’s do a couple of things to fix
that a bit.

First of all, we can add a custom icon so that our add-on doesn’t look like all
the other add-ons that haven’t bothered to set their icons…  To do that, we add
the following to `manifest.json` after the `manifest_version` line:

```json
  "icons": {
    "48": "icon.png",
    "128": "icon128.png"
  },
```

And, of course, we’ll need to download a pretty picture for our icon, so let’s
save a copy of [this picture][6b860aac] as `icon.png`, and [this one][9f391712]
as `icon128.png`.

We should also have a prettier icon for the button, so going back to the
`manifest.json`, let’s add the following lines in the `browser_action` block
before the `default_title`:

```json
    "default_icon": {
      "19": "button.png",
      "38": "button38.png"
    },
```

and save [this image][192a6d70] as `button.png`, and [this image][33c677fb] as
`button38.png`.

Finally, we need to tell our build script about the new files, so change the
`files` line of our `gulpfile.js` to:

```javascript
var files = ['manifest.json', 'background.js', '*.png'];
```

Re-run the build, and re-install the add-on, and [we’re done][01774107]!  😀

[![New, prettier, icons.](/images/blake/WebExtensions/HowTo/8-PrettyIcon.png)](/images/blake/WebExtensions/HowTo/large/8-PrettyIcon.png)

### One more thing…

Well, there is another thing we could try to do.  I mean, we have an add-on that
works beautifully in Firefox, but one of the advantages of the new WebExtension
API is that you can run the same add-on (or an add-on with minimal changes) on
both Firefox and Chrome.  So let’s see what it will take to get this running in
both browsers!

We’ll start by launching Chrome, and trying to load the add-on, and see what
errors it gives us.  To load our extension, we’ll need to go to
`chrome://extensions/`, and check the `Developer mode` checkbox, as shown below:

[![Now we’re hackers!](/images/blake/WebExtensions/HowTo/9-ChromeDeveloper.png)](/images/blake/WebExtensions/HowTo/large/9-ChromeDeveloper.png)

Then we can click the “Load unpacked extension…” button, and choose our
directory to load our add-on!  Uh-oh, it looks like we’ve got an error.

[![Close, but not quite.](/images/blake/WebExtensions/HowTo/10-ChromeAlmost.png)](/images/blake/WebExtensions/HowTo/large/10-ChromeAlmost.png)

Since the `applications` key is required for Firefox, I think we can safely
ignore this error.  And anyways, the button shows up!  And when we click it…

![Cats!](/images/blake/WebExtensions/HowTo/11-ChromeCats.gif)

So, I guess we’re done!  (I used to have a section in here about how to load
[babel.js][bf0735a9], because the version of Chrome I was using didn’t support
ES6’s [arrow functions][7a13d5e6], but apparently they upgraded their JavaScript
engine, and now everything is good.  😉)

Finally, if you have any questions, or run into any problems following this
tutorial, please feel free to leave a comment below, or get in touch with me
through [email][912ca5fb] or on [twitter][e2db8a87]!  If you have issues or
constructive feedback developing WebExtensions, the team will be listening on
the [Discourse forum][69d07c0d].

  [1ec53d8c]: https://wiki.mozilla.org/WebExtensions "Mozilla’s WebExtensions Wiki Page"
  [0fae7804]: https://developer.mozilla.org/en-US/Add-ons/WebExtensions "MDN’s WebExtensions Documentation"
  [f2b3806b]: https://developer.chrome.com/extensions "Chrome’s Extension API"
  [98536158]: https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Multiprocess_Firefox "a.k.a. Electrolysis"
  [4f9d6081]: https://nightly.mozilla.org/ "Download Nightly Here"
  [788ee3ee]: http://chilloutandwatchsomecatgifs.com/ "Cat Gifs!"
  [4063d915]: https://developer.chrome.com/extensions/manifest "Chrome’s Manifest Documentation"
  [d61ba671]: https://github.com/bwinton/catgif-extension/releases/tag/step-1 "Step One"
  [0f904c1a]: http://www.7-zip.org/ "7-Zip’s website"
  [533ab63e]: https://wiki.mozilla.org/Addons/Extension_Signing "Extension Signing Documentation"
  [7e996c37]: https://developer.chrome.com/extensions/browserAction "Chrome’s Browser Action Documentation"
  [9582f75d]: https://github.com/bwinton/catgif-extension/releases/tag/step-2 "Step Two"
  [157f3c41]: https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md#getting-started "Gulp’s Installation Instructions"
  [0686b7bc]: http://gulpjs.com/ "Gulp’s Homepage"
  [2fc43570]: https://nodejs.org/ "Node’s Homepage"
  [cb58b4da]: https://github.com/bwinton/catgif-extension/releases/tag/step-3 "Step Three"
  [a6089ff2]: https://github.com/bwinton/catgif-extension/releases/tag/step-4 "Step Four"
  [4b287c05]: https://github.com/bwinton/catgif-extension/releases/tag/step-5 "Step Five"
  [576c5422]: https://github.com/bwinton/catgif-extension/releases/tag/step-6 "Step Six"
  [6b860aac]: https://raw.githubusercontent.com/bwinton/catgif-extension/master/icon.png "icon.png"
  [9f391712]: https://raw.githubusercontent.com/bwinton/catgif-extension/master/icon128.png "icon128.png"
  [192a6d70]: https://raw.githubusercontent.com/bwinton/catgif-extension/master/button.png "button.png"
  [33c677fb]: https://raw.githubusercontent.com/bwinton/catgif-extension/master/button38.png "button38.png"
  [01774107]: https://github.com/bwinton/catgif-extension/releases/tag/step-7 "Step Seven"
  [bf0735a9]: https://babeljs.io/ "Babel!"
  [7a13d5e6]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions "a.k.a. Fat-Arrows."
  [912ca5fb]: mailto:bwinton@latte.ca "My email address"
  [e2db8a87]: https://twitter.com/bwinton/ "@bwinton"
  [69d07c0d]: https://discourse.mozilla-community.org/c/add-ons/development "Discourse: for all your communication needs."
