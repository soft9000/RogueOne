
''' Mission: Prevent confusion between various point references. '''

class Point:
    ''' Common usage paradigm. '''
    def __init__(self, zX, zY):
        self.x = zX; self.y = zY

    def equals(self, zobj):
        if not isinstance(zobj, Point):
            return False
        if self.x == zobj.x:
            if self.y == zobj.y:
                return True
        return False

class GridPoint(Point):
    ''' Marker Class
    The location for a cell on the screen. '''
    def __init__(self, zX, zY):
        super().__init__(zX, zY)

class GuiPoint(Point):
    ''' Marker Class
    The location for a point on the screen.
    -There usually many inside of a GridPoint. '''
    def __init__(self, zX, zY):
        super().__init__(zX, zY)
