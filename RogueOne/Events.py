#!/usr/bin/env python3

class Event:
    pass

class EventLoop:

    def __init__(self, char_up='e', char_down='v', char_left='a', char_right='c'):
        self.game_over = False
        self.reserved = "?!^&*><+-=@"
        self.actions = dict()
        self.actions[char_up]    = (char_up, "up", self.on_up)
        self.actions[char_down]  = (char_down, "down", self.on_down)
        self.actions[char_left]  = (char_left, "left", self.on_left)
        self.actions[char_right] = (char_right, "right", self.on_right)
        for key in self.actions:
            if key in self.reserved:
                raise Exception("Error: The key '" + key + "' is reserved.")
        self.actions['^'] = ('^', "jump", self.on_jump)
        self.actions['?'] = ('?', "help", self.on_help)
        self.actions['!'] = ('!', "quit", self.on_quit)

    def on_up(self, view):
        print("on_up")

    def on_down(self, view):
        print("on_down")

    def on_left(self, view):
        print("on_left")

    def on_right(self, view):
        print("on_right")

    def on_help(self, view):
        for key in self.actions:
            info = self.actions[key]
            print("'{}' = {}".format(info[0], info[1]))
        input(" --- enter ---")

    def on_quit(self, view):
        self.game_over = True

    def on_start(self, view):
        print("on_start")

    def on_jump(self, view):
        print("on_jump")

    def get_key(self, view):
        view.do_next()
        print(view.get_view())
        return input()
    
    def mainloop(self, view):
        self.on_start(view)
        while True:
            key = self.get_key(view)
            if key in self.actions:
                self.actions[key][2](view)
            if self.game_over:
                return True
        return False
