
from RogueOne.Shower import Shower

class Marker(Shower):
    ''' Markers DO NOT MOVE. '''
    def __init__(self, name, glyph, xpos, ypos):
        super().__init__(name, glyph, xpos, ypos)

    def on_next(self):
        ''' Process next turn (NO MOVE!) '''
        super().on_next()
    
        

