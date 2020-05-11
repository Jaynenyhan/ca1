#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def __str__(self):
        return 'Name: {}\nAge: {}\nMedications: {}\nDoctor: {}'.format(self.name, self.age, ', '.join(self.meds), self.doctor)

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

    def get_patients_by_medication(self, med):
        patients = []
        for name in self.d:
            if med in self.d[name].meds:
                patients.append(self.d[name])
        return patients
