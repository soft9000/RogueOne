import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../'))

from RogueOne.Shower import Shower

class Mover(Shower):
    def __init__(self, name, glyph, xpos, ypos):
        super().__init__(name, glyph, xpos, ypos)

    def on_move(self, xpos, ypos):
        ''' Relocate Mover '''
        self.location.x = xpos
        self.location.y = ypos

    def on_next(self):
        ''' Process next MOVEment '''
        super().on_next()

    
        

