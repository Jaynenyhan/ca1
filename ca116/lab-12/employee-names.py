#!/usr/bin/env python

# Get inputs
employees = []
s = raw_input()
while s != "end":
   employees.append(s)
   s = raw_input()

numbers = []
s = raw_input()
while s != "end":
   numbers.append(s)
   s = raw_input()

# For each employee number, check each item in list for the number
# If it exists, print that employees name then proceed to next number and repeat
