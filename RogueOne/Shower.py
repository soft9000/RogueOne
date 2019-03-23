
class Shower():
    ''' Fundamental piece - Mover, or Marker '''
    def __init__(self, name, glyph, xpos, ypos):
        self.name = name
        self.glyph = glyph
        self.location = [xpos, ypos]
        
    def on_next(self):
        pass

    def on_plot(self, view):
        view.plot(self.glyph, self.location[0], self.location[1])
