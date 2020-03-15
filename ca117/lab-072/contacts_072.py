#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return ' '.join((
            self.name, self.phone, self.email))

class ContactList(object):

    def __init__(self):
        self.d = {}

    def add_contact(self, contact):
        self.d[contact.name] = contact

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        try:
            return self.d[name]
        except KeyError:
            return None

    def __str__(self):
        sort = [str(self.d[x]) for x in sorted(self.d)]
        return '\n'.join(['Contact list', '------------'] + sort)

import sys

def main():
    cl = ContactList()
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)

    c = cl.get_contact('Jimmy')
    print(c)
    c = cl.get_contact('Mary')
    print(c)

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()
