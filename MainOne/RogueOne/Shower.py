import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../'))

from RogueOne.Points import GridPoint

class Shower():
    ''' Fundamental piece - Mover, or Marker '''
    def __init__(self, name, glyph, xpos, ypos):
        self.name = name
        self.glyph = glyph
        self.location = GridPoint(xpos, ypos)
        
    def on_next(self):
        pass

    def on_plot(self, view):
        view.plot(self.glyph, self.location)
