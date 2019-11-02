#!/usr/bin/env python

count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0

s = raw_input()
while s != "end":
   if s == "0":
      count_0 = count_0 + 1
   elif s == "1":
      count_1 = count_1 + 1
   elif s == "2":
      count_2 = count_2 + 1
   elif s == "3":
      count_3 = count_3 + 1
   elif s == "4":
      count_4 = count_4 + 1
   elif s == "5":
      count_5 = count_5 + 1
   elif s == "6":
      count_6 = count_6 + 1
   elif s == "7":
      count_7 = count_7 + 1
   elif s == "8":
      count_8 = count_8 + 1
   elif s == "9":
      count_9 = count_9 + 1
   s = raw_input()

print 0, "*" * count_0
print 1, "*" * count_1
print 2, "*" * count_2
print 3, "*" * count_3
print 4, "*" * count_4
print 5, "*" * count_5
print 6, "*" * count_6
print 7, "*" * count_7
print 8, "*" * count_8
print 9, "*" * count_9
