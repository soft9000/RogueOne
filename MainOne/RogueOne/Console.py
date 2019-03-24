
from RogueOne.Rectangle import Rectangle
from RogueOne.View import View

PLAYER = "Player"

class ConsoleApplication(Rectangle):   
    '''
    The READILY visible aspect / viewport over your
    simulation (i.e. actual area / map could be
    A LOT larger!)
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
        ''' Process the next turn. Return False to end the game. '''
        # Givers FIRST
        for key in self.resources:
            self.resources[key].on_next()
        for key in self.markers:
            self.markers[key].on_next()
        # Takers LAST
        for key in self.movers:
            self.movers[key].on_next()
        return True

    def _get_player(self):
        global PLAYER
        if PLAYER in self.movers:
            return self.movers[PLAYER]
        return None
    
    def do_up(self, view):
        player = self._get_player()
        if player:
            player.on_move(player.location[0], player.location[1] - 1)

    def do_down(self, view):
        player = self._get_player()
        if player:
            player.on_move(player.location[0], player.location[1] + 1)

    def do_left(self, view):
        player = self._get_player()
        if player:
            player.on_move(player.location[0] - 1, player.location[1])

    def do_right(self, view):
        player = self._get_player()
        if player:
            player.on_move(player.location[0] + 1, player.location[1])
        
    def on_plot(self, view):
        '''
        Draw the screen. Will be called after the game is over
        (i.e. do_next() returns False) so as to allow us to
        display gameplay results (etc.)
        '''
        view.clear_screen()
        # Givers FIRST
        for key in self.resources:
            self.resources[key].on_plot(view)
        for key in self.markers:
            self.markers[key].on_plot(view)
        # Takers LAST
        for key in self.movers:
            self.movers[key].on_plot(view)
        view.show_screen()    

