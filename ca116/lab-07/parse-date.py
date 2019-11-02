#!/usr/bin/env python

s = raw_input()

space1 = 0
while space1 < len(s) and s[space1] != " ":
   space1 = space1 + 1

space2 = space1 + 1
while space2 < len(s) and s[space2] != " ":
   space2 = space2 + 1

space3 = space2 + 1
while space3 < len(s) and s[space3] != " ":
   space3 = space3 + 1

day = s[:space1]
date = s[space1 + 1:space2]
month = s[space2 + 1:space3 - 1]
year = s[space3 + 1:]

print month, date + ",", year, "(" + day + ")"
