#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        return 'Name: {}\nAge: {}\nDoctor: {}'.format(self.name, self.age, self.doctor)
