#!/usr/bin/env python3

class Time(object):

    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def __str__(self):
        return 'The time is {:02d}:{:02d}:{:02d}'.format(
            self.hour, self.minute, self.second)

    def __eq__(self, other):
        return self.time_to_seconds() == other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        seconds = self.time_to_seconds() + other.time_to_seconds()
        return Time.seconds_to_time(seconds)

    def __iadd__(self, other):
        seconds = self.time_to_seconds() + other.time_to_seconds()
        new = Time.seconds_to_time(seconds)
        self.hour = new.hour
        self.minute = new.minute
        self.second = new.second
        return self

    def time_to_seconds(self):
        minutes = self.minute + self.hour * 60
        seconds = self.second + minutes * 60
        return seconds

    @classmethod
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        days, hour = divmod(hour, 24)
        return cls(hour, minute, second)

def main():

    t1 = Time()
    t2 = Time(9, 35, 16)
    t3 = Time(0, 0, 4)
    t4 = Time(9, 35, 16)

    # Check string representation
    print('Printing times...')
    print(t1)
    print(t2)
    print(t3)

    # Check equality
    print('Checking equality...')
    print(t2 == t4)
    print(t1 == t3)

    # Check greater than/less than
    print('Checking greater than/less than...')
    print(t2 > t3)
    print(t2 < t3)
    print(t4 > t1)
    print(t4 < t1)

    # Check addition
    print('Checking addition...')
    t5 = t2 + t2 + t2
    print(t5)
    print(t5 > t2)

    # Check increment
    print('Checking increment...')
    t33 = t2
    t2 += t2
    t2 += t4
    print(t2)
    print(t33 is t2)
    print(t2 > t3)

    # Check class method
    print('Checking class method...')
    t6 = Time.seconds_to_time(123456)
    print(t6)
    print(t6 > t1)

if __name__ == '__main__':
    main()
