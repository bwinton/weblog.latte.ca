#!/bin/bash
set -e # exit with nonzero exit code if anything fails
# set -x # debug stuff to see what fails.

# clear the dist directory
rm -rf dist || exit 0;
rm -rf git || exit 0;

# get the existing gh-pages history, but clean out the files.
git clone --quiet --branch=gh-pages https://${GH_TOKEN}@${GH_REF} dist > /dev/null
cd dist

mkdir ../git
cp -r .git ../git
if [ -f .doit.db ]; then
  cp .doit.db ..
fi
if [ -d cache ]; then
  cp -r cache ..
fi
cd ..

# run our compile script, discussed above
nikola build
set +e # ignore the next error…
nikola check --clean-files
set -e # exit with nonzero exit code if anything fails

# inside the gh-pages repo we'll pretend to be a new user
cd dist
cp -r ../git/.git .
cp ../.doit.db .
cp -r ../cache .

git config user.name "Travis CI"
git config user.email "weblog@latte.ca"

if [ -n "$(git status --porcelain)" -a "${TRAVIS_PULL_REQUEST}" == "false" ]; then
  git add -Af .
  git commit -m "Deploy ${TRAVIS_COMMIT_RANGE} to GitHub Pages."

  # Force push from the current repo's master branch to the remote
  # repo's gh-pages branch. (All previous history on the gh-pages branch
  # will be lost, since we are overwriting it.) We redirect any output to
  # /dev/null to hide any sensitive credential data that might otherwise be exposed.
  git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" gh-pages
fi
