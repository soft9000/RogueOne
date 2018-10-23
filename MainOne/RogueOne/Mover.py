
from RogueOne.Shower import Shower

class Mover(Shower):
    def __init__(self, name, glyph, xpos, ypos):
        super().__init__(name, glyph, xpos, ypos)

    def on_move(self, xpos, ypos):
        ''' Relocate Mover '''
        self.location[0] = xpos
        self.location[1] = ypos

    def on_next(self):
        ''' Process next MOVEment '''
        super().on_next()

    
        

