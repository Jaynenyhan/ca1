#!/usr/bin/env python3

class Student(object):

    def __init__(self, surname, forename, sid, modlist=[]):
        self.surname = surname
        self.forename = forename
        self.sid = sid
        self.modlist = modlist

    def add_module(self, mod):
        if mod not in self.modlist:
            self.modlist.append(mod)

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)

    def print_details(self):
        print('ID: {}\nSurname: {}\nForename: {}\nModules: {}'.format(
            self.sid, self.surname, self.forename, " ".join(self.modlist)))
