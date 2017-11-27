#!usr/bin/env python

from Queue import PriorityQueue

class State(object):
    def __init__(self, value, parent,
                    start=0, goal = 0, solver = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
            self.solver = parent.solver
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
            self.solver = solver

    def GetDist(self):
        pass
    def CreateChildren(self):
        pass

class State_string(State):
