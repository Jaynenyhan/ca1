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

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        a = []
        a.append('Name: {}'.format(self.name))
        a.append('ID: {}'.format(self.tid))
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
