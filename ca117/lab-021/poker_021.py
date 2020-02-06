#!/usr/bin/env python3

import sys

def poker(lines):
   ranks = {
      0: "nothing",
      1: "one pair",
      2: "two pairs",
      3: "three of a kind",
      4: "a straight",
      5: "a flush",
      6: "a full house",
      7: "four of a kind",
      8: "a straight flush",
      9: "a royal flush",
   }
   count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
   total = len(lines)
   for line in lines:
      s = line.strip()
      count[int(s[-1])] += 1
   for i in ranks:
      print("The probability of {} is {:.4f}%".format(ranks[i], count[i] / total * 100))

def main():
   poker(sys.stdin.readlines())

if __name__ == '__main__':
   main()
