
from RogueOne.Rectangle import Rectangle
from RogueOne.View import View

class ConsoleApplication(Rectangle):
    '''
    The READILY visible aspect / viewport over your
    simulation (i.e. actual area / map could be
    ALLOT larger!)
    '''
    def __init__(self):
        super().__init__(80,25)
        self.movers  = dict()
        self.markers = dict()
        self.resources = dict()

    def add_mover(self, mover):
        ''' Add a console Mover '''
        self.movers[mover.name] = mover       

    def add_marker(self, marker):
        ''' Add a map / simulation Marker '''
        self.markers[marker.name] = marker

    def add_resource(self, res):
        ''' Add a potenital player resource '''
        self.resources[res.name] = res

    def do_next(self):
        ''' Process the next turn '''
        # Givers FIRST
        for key in self.resources:
            self.resources[key].on_next()
        for key in self.markers:
            self.markers[key].on_next()
        # Takers LAST
        for key in self.movers:
            self.movers[key].on_next()

    def get_view(self, view=None):
        if view is None:
            view = View(' ', self.width, self.height)
        else:
            view.clear_screen()
        # Givers FIRST
        for key in self.resources:
            self.resources[key].on_plot(view)
        for key in self.markers:
            self.markers[key].on_plot(view)
        # Takers LAST
        for key in self.movers:
            self.movers[key].on_plot(view)
            
        return view
    

