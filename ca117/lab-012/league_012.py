#!/usr/bin/env python3

import sys

def league(teams):
   longest = len(" ".join(teams[0][1:-8]))
   for team in teams:
      club = " ".join(team[1:-8])
      if len(club) > longest:
         longest = len(club)
   print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format("POS", "CLUB", longest, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))
   for team in teams:
      pos = team[0]
      club = " ".join(team[1:-8])
      p = team[-8]
      w = team[-7]
      d = team[-6]
      l = team[-5]
      gf = team[-4]
      ga = team[-3]
      gd = team[-2]
      pts = team[-1]

      print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(pos, club, longest, p, w, d, l, gf, ga, gd, pts))

def main():
   teams = []
   for line in sys.stdin:
      teams.append(line.split())
   league(teams)

if __name__ == '__main__':
   main()
