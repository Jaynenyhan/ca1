#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, athlete):
        self.d[athlete.tid] = athlete

    def remove(self, athlete):
        del self.d[athlete]

    def lookup(self, athlete):
        return self.d.get(athlete)

    def sort(tuple):
        (_, v) = tuple
        return v.name

    def __str__(self):
        a = []
        for k, v in sorted(self.d.items(), key=Triathlon.sort):
            a.append(str(v))
        return '\n'.join(a)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
