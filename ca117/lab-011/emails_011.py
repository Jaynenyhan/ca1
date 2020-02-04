#!/usr/bin/env python3

import sys

def names(s):
   no_digits = ""
   for c in s:
      if not c.isdigit():
         no_digits += c
   name_list = "".join(no_digits).split("@")[0].split(".")
   new_words = []
   for word in name_list:
      new_words.append(word.capitalize())
   name = " ".join(new_words)
   print(name)

def main():
   for line in sys.stdin:
      s = line.strip()
      names(s)

if __name__ == '__main__':
   main()
