#!/usr/bin/env python3

import sys
import math

def main():
   start_r = float(sys.argv[1])
   inc_r = float(sys.argv[2])
   end_r = float(sys.argv[3])

   h1 = 'Radius (m)'
   h1_len = '-' * len(h1)
   h2 = 'Area (m^2)'
   h2_len = '-' * len(h2)
   h3 = 'Volume (m^3)'
   h3_len = '-' * len(h3)

   print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
   print('{:>s} {:>15s} {:>15s}'.format(h1_len, h2_len, h3_len))

   while start_r <= end_r:
      area = 4 * math.pi * start_r ** 2
      volume = (4 / 3) * math.pi * start_r ** 3

      print('{:>10.1f} {:>15.2f} {:>15.2f}'.format(start_r, area, volume))

      start_r += inc_r

if __name__ == '__main__':
   main()
