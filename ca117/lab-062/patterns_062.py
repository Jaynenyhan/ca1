#!/usr/bin/env python3

from re import findall
import sys

date = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2}\b'
phone = r'\b01[-\s]\d{7}\b'
email = r'\b(?:\w|\.)*@(?:\w|\.)*.\w*\b'
ldate = r'\b\d{1,2}\s\w{3}\s\d{2}\b'

def main():

    # Verify regular expressions are not overly long
    assert(len(date) < 40)
    assert(len(phone) < 40)
    assert(len(email) < 40)
    assert(len(ldate) < 80)

    s = sys.stdin.read()

    datelist = findall(date, s)
    print('Dates: {}'.format(datelist))

    phonelist = findall(phone, s)
    print('Phones: {}'.format(phonelist))

    emaillist = findall(email, s)
    print('Emails: {}'.format(emaillist))

    ldatelist = findall(ldate, s)
    print('Long dates: {}'.format(ldatelist))

if __name__ == '__main__':
    main()
