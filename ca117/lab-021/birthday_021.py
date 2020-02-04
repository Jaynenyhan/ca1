#!/usr/bin/env python3

import sys
import calendar

def birthday(day, month, year):
   poem = [
      "Monday's child is fair of face.",
      "Tuesday's child is full of grace.",
      "Wednesday's child is full of woe.",
      "Thursday's child has far to go.",
      "Friday's child is loving and giving.",
      "Saturday's child works hard for a living.",
      "Sunday's child is fair and wise and good in every way.",
   ]
   day = calendar.weekday(year, month, day)
   print("You were born on a {} and {}".format(calendar.day_name[day], poem[day]))

def main():
   [day, month, year] = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
   birthday(day, month, year)

if __name__ == '__main__':
   main()
