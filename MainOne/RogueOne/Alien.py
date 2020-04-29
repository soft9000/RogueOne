
from RogueOne.Noun import Noun
from RogueOne.Points import GridPoint as GridPoint
from RogueOne.NavCalc import NavCalc as NavCalc

class Alien(Noun):

    def __init__(self, name, glyph, xpos, ypos, map_width, map_height):
        super().__init__(name, glyph, xpos, ypos)
        self.nav = NavCalc(xpos, ypos)
        self.map_width = map_width
        self.map_height = map_height
        self.nav.plot(xpos, ypos)
        self.id = None

    def on_plot(self, parent):
        super().on_plot(parent)
        gui = parent.grid2gui(self.location)
        if self.id:
            parent.canvas.delete(self.id)
        self.id = parent.canvas.create_arc(
            gui.x - 20, gui.y - 20,
            gui.x + 20, gui.y + 10,
            style='arc', start="0.1", extent='359',
            outline='green', width='2')
        course = self.nav.next()
        if not course[0]:
            self.location.x = course[1].x
            self.location.y = course[1].y
        else:
            x = self.nav.rnd.randrange(0, self.map_width)
            y = self.nav.rnd.randrange(0, self.map_height)
            self.nav.plot(x, y)
