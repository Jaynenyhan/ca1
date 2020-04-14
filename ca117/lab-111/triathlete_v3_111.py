#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.discipline = {
            'swim': None,
            'run': None,
            'cycle': None
        }

    def __str__(self):
        a = []
        a.append('Name: {}'.format(self.name))
        a.append('ID: {}'.format(self.tid))
        a.append('Race time: {}'.format(self.total_time()))
        return '\n'.join(a)

    def add_time(self, discipline, time):
        self.discipline[discipline] = time

    def get_time(self, discipline):
        return self.discipline[discipline]

    def total_time(self):
        return sum(self.discipline.values())

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __lt__(self, other):
        return self.total_time() < other.total_time()

    def __gt__(self, other):
        return self.total_time() > other.total_time()

def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)

if __name__ == '__main__':
    main()
