#!/usr/bin/env python

# Get inputs
a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

# Manipulate data
dates = []
names = []
i = 0
while i < len(a):

   curr = a[i]

   curryear = curr[6:8]
   currmonth = curr[3:5]
   currday = curr[0:2]
   currdate = curryear + currmonth + currday
   dates.append(currdate)

   currname = curr[9:]
   names.append(currname)

   i = i + 1

# Sort dates
i = 0
while i < len(dates):

   smallest = i

   j = i + 1
   while j < len(dates):
      if dates[j] < dates[smallest]:
         smallest = j
      j = j + 1

# Edit dates list
   tmp = dates[i]
   dates[i] = dates[smallest]
   dates[smallest] = tmp

# Edit names list accordingly
   tmp = names[i]
   names[i] = names[smallest]
   names[smallest] = tmp

   i = i + 1

i = 0
while i < len(names):
   print names[i]
   i = i + 1
