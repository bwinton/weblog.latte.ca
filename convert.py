#!/usr/bin/env python

from datetime import datetime
import os
from optparse import OptionParser
from collections import OrderedDict
import pwd
import sys

def getStats(source):
  stat = os.stat(source)
  date = datetime.fromtimestamp(stat.st_mtime).isoformat(" ")

  author = pwd.getpwuid(stat.st_uid).pw_gecos

  return (date, author)

def handleMarkdown(source, dest):
  print "  MKD: " + source + " -> " + dest

  date, author = getStats(source)

  data = open(source).read()
  title, next, data = data.split("\n", 2)
  tags = ""
  if next.startswith("#"):
    tags = next.replace("#tags ", "", 1).replace(" ", ", ").lower()
    next, data = data.split("\n", 1)
  while next.strip() == "":
    next, data = data.split("\n", 1)
  data = next + "\n" + data

  metadata = OrderedDict([
    ("title", title),
    ("date", date),
    ("author", author)
  ])
  if tags:
    metadata["tags"] = tags
  header = "\n".join(".. " + key + ": " + value for key,value in metadata.items())

  output = open(dest, "w")
  output.write("""<!--
%s
-->

%s
""" % (header, data))


def main(argv=None):
  if argv is None:
    argv = sys.argv
  parser = OptionParser()

  (options, args) = parser.parse_args()

  if len(args) < 2:
    print >> sys.stderr, "Need <source> and <dest> as arguments."
    return 1

  source = args[0]
  dest = args[1]
  print "Copying from " + source + " to " + dest + "."

  for directory, dirnames, filenames in os.walk(source):
    output = directory.replace(source, dest, 1)
    if not os.path.exists(output):
      os.makedirs(output)
    print directory + " -> " + output
    for filename in filenames:
      if filename.endswith(".md"):
        handleMarkdown(os.path.join(directory, filename), os.path.join(output, filename))
      elif filename.endswith(".txt"):
        handleMarkdown(os.path.join(directory, filename), os.path.join(output, filename))

  return 0

if __name__ == "__main__":
  sys.exit(main())