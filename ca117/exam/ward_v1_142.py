#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        return 'Name: {}\nAge: {}\nDoctor: {}'.format(self.name, self.age, self.doctor)

class Ward(object):

    def __init__(self):
        self.d = {}

    def add(self, patient):
        self.d[patient.name] = patient

    def remove(self, name):
        del self.d[name]

    def lookup(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None
