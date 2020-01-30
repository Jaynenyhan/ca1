#!/usr/bin/env python3

import sys

def names(line):
   no_digits = []
   for i in line:
      if not i.isdigit():
         no_digits.append(i)
   name_list = "".join(no_digits).split("@")[0].split(".")
   new_words = []
   for word in name_list:
      new_words.append(word.capitalize())
   name = " ".join(new_words)
   return name

def main():
   for line in sys.stdin:
      output = names(line)
      print(output)

if __name__ == '__main__':
   main()
