#!/usr/bin/env python3

import sys

def time2mins(time):
    hours, mins = [int(i) for i in time.split(':')]
    return hours * 60 + mins

def mins2time(mins):
    hours = mins // 60
    mins = mins % 60
    if hours < 0:
        hours += 24
    elif hours == 24:
        hours = 0
    return '{:02d}:{:02d}'.format(hours, mins)

def time_calc(time, mins):
    time_mins = time2mins(time)
    new_time = mins2time(time_mins - int(mins))
    return new_time

def main():
    for line in sys.stdin:
        time, mins = line.split()
        print(time_calc(time, mins))

if __name__ == "__main__":
    main()
