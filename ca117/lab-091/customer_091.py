#!/usr/bin/env python3

class Customer(object):

    discount = 0

    def __init__(self, name, bal, a1, a2, a3):
        self.name = name
        self.balance = bal
        self.addr_line1 = a1
        self.addr_line2 = a2
        self.addr_line3 = a3

    def owes(self):
        return self.balance - self.balance * self.discount

    def __str__(self):
        a = []
        a.append(self.name)
        a.append(self.addr_line1)
        a.append(self.addr_line2)
        a.append(self.addr_line3)
        a.append('Balance: {:.2f}'.format(self.balance))
        a.append('Discount: {:.0f}%'.format(self.discount * 100))
        a.append('Amount due: {:.2f}'.format(self.owes()))
        return '\n'.join(a)

class ValuedCustomer(Customer):

    discount = 0.1

def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare')
    c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon')
    c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry')

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()
