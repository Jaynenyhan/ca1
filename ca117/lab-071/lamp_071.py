#!/usr/bin/env python3

class Lamp(object):

    def __init__(self, boolean=False):
        self.on = boolean

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True
