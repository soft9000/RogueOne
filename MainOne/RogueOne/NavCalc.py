# Inspired by https://github.com/soft9000/Rogueish.NET/blob/master/Rogueish1/NavCalc.cs

from RogueOne.Points import GridPoint as GridPoint
from random import Random as Random

class NavCalc():

    ''' A navigational computer, worthy of Player / NPC / AI usage. 
    -Just enough random to allow different plots to destination(s)
    so as to better simulate different realities.
    '''

    def __init__(self, startX=0, startY=0, destX=0, destY=0):
       self.here = GridPoint(startX, startY)
       self.there = GridPoint(destX, destY)
       self.course = GridPoint(-1,-1)
       self.rnd = Random()
       self.rnd.seed()

    def plot(self, x, y):
        self.there.x = x
        self.there.y = y

    def next(self):
        ''' Returns 2-tuple:. 0 is True upon arrival, 1 is point to 'nav to.'''
        next = self.here
        if next.equals(self.there):
            return True, GridPoint(self.there.x, self.there.y) # there

        self.course.x = self.there.x - self.here.x
        self.course.y = self.there.y - self.here.y
        trend = self.rnd.randint(1,3)
        if trend == 1:
            next.x = self.inc(self.course.x, next.x)
        elif trend == 2:
            next.y = self.inc(self.course.y, next.y)
        else:
            next.x = self.inc(self.course.x, next.x)
            next.y = self.inc(self.course.y, next.y)

        return False, GridPoint(next.x, next.y) # not there

    def inc(self, posneg, location):
        if posneg > 0:
            return location + 1
        elif posneg < 1:
            return location - 1
        return location



