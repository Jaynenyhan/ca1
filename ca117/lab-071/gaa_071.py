#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.total = goals * 3 + points

    def greater_than(self, other):
        if self.total > other.total:
            return True
        else:
            return False

    def less_than(self, other):
        if self.total < other.total:
            return True
        else:
            return False

    def equal_to(self, other):
        if self.total == other.total:
            return True
        else:
            return False
