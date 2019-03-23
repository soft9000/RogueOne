
from RogueOne.Rectangle import Rectangle

class View(Rectangle):
    """ A mutable, as well as string representable, view. """

    def __init__(self, default_glyph, xpos, ypos):
        """ Create a mutable, yet displayable, unicode map. """
        super().__init__(xpos, ypos)
        self.glyph = default_glyph
        self.screen = list()
        for row in range(ypos):
            self.screen.append([self.glyph] * xpos)

    def clear_screen(self, char=None):
        """ Reset a unicode map to the default character value. """
        value = self.glyph
        if char is not None:
            value = char
        for row in self.screen:
            for col in range(len(row)):
                row[col] = char

    def plot(self, glyph, xpos, ypos):
        """ Set a coordinate to a unicode character. """
        if glyph is None:
            glyph = self.glyph
        self.screen[ypos][xpos] = glyph

    def __str__(self):
        """ Generate a console-printable, immutable, unicode string. """
        from io import StringIO
        result = StringIO()
        for row in self.screen:
            for col in range(len(row)):
                result.write(row[col])
            result.write('\n')
        zstr = result.getvalue()
        result.close()
        return zstr

    def __repr__(self):
        """ Creae a eval()uable, and mutable, representation."""
        return str(self.screen)
        

if __name__ == "__main__":
    wide = 10
    high = wide + 2
    view = View('?', wide, high)
    print(str(view))
    view.clear_screen("..")

    for x in range(wide):
        view.plot(chr(3222 + x), x, x)

    for ss, line in enumerate(view.screen, 1):
        print(ss, line)

    print(str(view))
    print(repr(view))
