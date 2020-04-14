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

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
