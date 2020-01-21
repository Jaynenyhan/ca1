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
# If it exists, print that employees name and repeat
i = 0
while i < len(numbers):
   j = 0
   while j < len(employees):
      if numbers[i] == employees[j][:8]:
         print employees[j][9:]
      j += 1
   i += 1
