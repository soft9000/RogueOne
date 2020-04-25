from RogueOne.Rectangle import Rectangle

PLAYER = "Player"

class Event:
    ''' Add a key-level event into the loop - see set_KeyEvent(below) '''
    def __init__(self, keyChar, helpStr, on_call):
        self.keyChar = keyChar
        self.helpStr = helpStr
        self.on_call = on_call


class ConsoleApplication(Rectangle):   
    '''
    The READILY visible aspect / viewport over your
    simulation (i.e. actual area / map could be
    A LOT larger!)
    '''
    def __init__(self, char_up='Up', char_down='Down', char_left='Left', char_right='Right'):
        super().__init__(80,25)
        self.game_over  = False
        self.parent = None
        self.movers  = dict()
        self.markers = dict()
        self.resources = dict()
        self.actions    = dict()
        self.set_KeyEvent(Event(char_up, "up", self.do_up))
        self.set_KeyEvent(Event(char_down, "down", self.do_down))
        self.set_KeyEvent(Event(char_left, "left", self.do_left))
        self.set_KeyEvent(Event(char_right, "right", self.do_right))
        self.set_KeyEvent(Event('?', "help", self.do_help))
        self.set_KeyEvent(Event('F1', "help", self.do_help))
        self.set_KeyEvent(Event('End', "quit", self.do_quit))

    def set_Parent(self, parent):
        self.parent = parent

    def set_KeyEvent(self, event):
        ''' Support user-assignable, single-key, events '''
        if isinstance(event, Event) is False:
            return False
        self.actions[event.keyChar] = event
        return True

    def get_KeyEvents(self):
        return list(self.actions.keys())

    def event_MouseClick(self, button, xpos, ypos):
        print(button, xpos, ypos)

    def event_KeyPress(self, key, xpos, ypos):
        print(key, xpos, ypos)
        if key in self.actions:
            action = self.actions[key].on_call
            if action:
                action()
        if not self.game_over:
            self.event_gameStep()

    def event_gameStep(self):
        if self.do_next() is False:
            self.game_over = True
        else:
            self.on_plot()

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
    
    def do_up(self):
        player = self._get_player()
        if player:
            player.on_move(player.location.x, player.location.y - 1)

    def do_down(self):
        player = self._get_player()
        if player:
            player.on_move(player.location.x, player.location.y + 1)

    def do_left(self):
        player = self._get_player()
        if player:
            player.on_move(player.location.x - 1, player.location.y)

    def do_right(self):
        player = self._get_player()
        if player:
            player.on_move(player.location.x + 1, player.location.y)

    def do_help(self):
        for key in self.actions:
            info = self.actions[key]
            print("'{}' = {}".format(info.keyChar, info.helpStr))
 
    def do_quit(self):
        self.game_over = True
        if self.parent:
            self.parent.stop()
       
    def on_plot(self):
        '''
        Draw the screen. Will be called after the game is over
        (i.e. do_next() returns False) so as to allow us to
        display gameplay results (etc.)
        '''
        if self.parent:
            self.parent.clear_screen()
        # Givers FIRST
        for key in self.resources:
            self.resources[key].on_plot(self.parent)
        for key in self.markers:
            self.markers[key].on_plot(self.parent)
        # Takers LAST
        for key in self.movers:
            self.movers[key].on_plot(self.parent)
        if self.parent:
            self.parent.show_screen()    

