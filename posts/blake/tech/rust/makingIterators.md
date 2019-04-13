<!--
.. title: Neat new feature in Rust…
.. date: 2019-04-13 16:49:00
.. author: Blake Winton
.. tags: adventofcode, rust, iterators, generators
-->

A few years ago, I decided to try my hand at the
[Advent of Code](https://adventofcode.com/) problems in Rust, as a way to help me
learn the language. One of the things I like to do in Rust (which I also liked to do
in Python) is make heavy use of iterators, so when I come up against a problem
[like this](https://adventofcode.com/2017/day/3), I reach for them first!

<!-- TEASER_END -->

Unfortunately, creating an iterator in Rust is kind of a pain in the butt.
Fortunately, Rust lets you write macros to help smooth off some of the rough edges,
so I took at stab at it, and talked to my co-worker Nika about it, and she
eventually wrote
[this](https://play.rust-lang.org/?gist=0cbc09e0fc41016f5f5c240d088a4410&version=stable),
which was a lot of help!

But recently Rust has introduced a
[couple of new features](https://blog.rust-lang.org/2019/04/11/Rust-1.34.0.html#library-stabilizations),
and the one that caught my eye in particular was
[`std::iter::from_fn`](https://doc.rust-lang.org/std/iter/fn.from_fn.html),
which let’s you make an iterator from a function, which is most of what that
macro was trying to do, so I thought I would try to convert the various places
I was using the macro to use the new function instead…

The first one I tried converting was `FactorsIter`, an iterator of arrays of
factors of the integers. It looked like like this:
``` rust
define_iterator!(FactorsIter (
    &curr: usize = 1
  ) -> Option<HashSet<usize>> {

  let mut factors = HashSet::new();
  let upper_limit = (*curr as f64).sqrt() as usize + 1;
  for i in 1..upper_limit {
    if *curr % i == 0 {
      factors.insert(i);
      factors.insert(*curr / i);
    }
  }
  *curr += 1;
  Some(factors)
});
//…
    for (i, factors) in FactorsIter::default().enumerate() {
```

and turned into something like this:
``` rust
fn factors_iter() -> impl Iterator<Item = HashSet<usize>> {
    let mut curr: usize = 1;

    std::iter::from_fn(move || {
        let mut factors = HashSet::new();
        let upper_limit = (curr as f64).sqrt() as usize + 1;
        for i in 1..upper_limit {
            if curr % i == 0 {
                factors.insert(i);
                factors.insert(curr / i);
            }
        }
        curr += 1;
        Some(factors)
    })
}
// …
    for (i, factors) in factors_iter().enumerate() {
```
Not a huge change, but it does read a little nicer to me.

The next one was the `HundredIter`, which took a number of ingredients, and
returned each combination of them that would add up to 100 total items. It
started off as:
``` rust
define_iterator!(HundredIter (
    &curr: Vec<i32> = vec![],
    &max: i32 = 100,
    &len: usize = 0
  ) -> Option<Vec<i32>> {

  let curr_len = *len - 1;
  if curr.is_empty() {
    for _ in 0..curr_len {
      curr.push(0)
    }
  } else {
    curr[curr_len - 1] += 1;
  }

  if curr[0] == *max {
    return None;
  }

  let mut rest: i32 = *max - curr.iter().sum::<i32>();

  let mut found = false;
  while rest < 0 {
    for i in 1..curr_len {
      if curr[curr_len - i] != 0 {
        found = true;
        curr[curr_len - i] = 0;
        curr[curr_len - i - 1] += 1;
        break;
      }
    }
    if !found {
      break;
    }
    rest = *max - curr.iter().sum::<i32>();
  }
  if !found && rest < 0 {
    None
  } else {
    let mut rv = curr.clone();
    rv.push(rest);

    Some(rv)
  }
});
```

which is _fine_, I guess, but not great. It ended up as:

``` rust
fn hundred_iter(len: usize) -> impl Iterator<Item = Vec<i32>> {
    let mut curr: Vec<i32> = vec![];
    const MAX: i32 = 100;
    let curr_len: usize = len - 1;

    std::iter::from_fn(move || {
        if curr.is_empty() {
            for _ in 0..curr_len {
                curr.push(0)
            }
        } else {
            curr[curr_len - 1] += 1;
        }

        if curr[0] == MAX {
            return None;
        }

        let mut rest: i32 = MAX - curr.iter().sum::<i32>();

        let mut found = false;
        while rest < 0 {
            for i in 1..curr_len {
                if curr[curr_len - i] != 0 {
                    found = true;
                    curr[curr_len - i] = 0;
                    curr[curr_len - i - 1] += 1;
                    break;
                }
            }
            if !found {
                break;
            }
            rest = MAX - curr.iter().sum::<i32>();
        }
        if !found && rest < 0 {
            None
        } else {
            let mut rv = curr.clone();
            rv.push(rest);

            Some(rv)
        }
    })
}
```

which seems a lot better. I mean, the code itself is almost identical (the
main difference being we don’t have any weird `*`s hanging around), but it’s
_much_ clearer which parts of the signature are supposed to be parameters,
and which are variables that we use to keep track of state!

Calling it is much nicer, too, going from:
``` rust
    let iter = HundredIter {
        len: ingredients.len() as usize,
        ..Default::default()
    };
```

to the much more obvious:
``` rust
    let iter = hundred_iter(ingredients.len());
```
😃

Oh, and here’s
[the new version](https://play.rust-lang.org/?version=stable&edition=2018&gist=06e6c23744270c1a78357658a33fc9b3)
of the gist above. It’s not a huge change, but it’s a little simpler, and
feels a little more Rust-y to me.