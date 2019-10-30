#!/usr/bin/env python

mark = input()

## first >= 70
## second >= 50
## second < 70
## third >= 40
## third < 50
## fail < 40

print "first:", mark >= 70
print "second:", mark >= 50 and mark < 70
print "third:", mark >= 40 and mark < 50
print "fail:", mark < 40
