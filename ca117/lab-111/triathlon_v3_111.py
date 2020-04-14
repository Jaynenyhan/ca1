#!/usr/bin/env python3

class Triathlon(object):

    def __init__(self, d={}):
        self.d = d

    def add(self, athlete):
        self.d[athlete.tid] = athlete

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        return self.d.get(tid)

    def sort(kv):
        (k, v) = kv
        return v.name

    def __str__(self):
        a = []
        for (k, v) in sorted(self.d.items(), key=Triathlon.sort):
            a.append(str(v))
        return '\n'.join(a)

    def times(self):
        times = []
        for (k, v) in self.d.items():
            times.append([v.total_time(), v.tid])
        return times

    def best(self):
        return self.d[min(self.times())[1]]

    def worst(self):
        return self.d[max(self.times())[1]]

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

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
