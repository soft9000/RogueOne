
from RogueOne.Noun import Noun

class ShipOne(Noun):

    def __init__(self, name, glyph, xpos, ypos):
        super().__init__(name, glyph, xpos, ypos)
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
            outline='red', width='3')
        

