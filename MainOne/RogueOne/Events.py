#!/usr/bin/env python3

from collections import OrderedDict
from tkinter import *


class Event:
    pass

class EventLoop(Tk):
    
    ''' The TK window that we will use for drawing, as well as managing input events. '''

    def __init__(self, char_up='e', char_down='c', char_left='s', char_right='f', width=800, height=600):
        super().__init__()
        self.font_sz    = 16
        self.width      = width
        self.height     = height
        self.cell_width = int(width / 10)
        self.cell_height= int(height / 10)
        self.screen     = None
        self.screen_rows= list()
        self.view       = None
        self.canvas     = None
        self.font       = None
        self.game_over  = False
        self.reserved   = "?!^&*><+-=@"
        self.actions    = dict()
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

    def start(self):
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.bind_all('<KeyPress>', self.event_KeyPress, '+')
        self.canvas.pack()
        self.clear_screen()
        self.font = ("Courier", self.font_sz, "bold")
        super().mainloop()

    def clear_screen(self):
        ''' Fills the internal screen-buffer with the default character. '''
        self.screen = [[' '] * self.cell_width
                       for yy in range(self.cell_height * 2)]
        if len(self.screen_rows) is 0:
            for rowy in range(self.cell_height):
                zid = self.canvas.create_text(10, (rowy * self.font_sz) + 10,
                                        anchor='w', font=self.font)
                self.screen_rows.append(zid) 

    def show_screen(self):
        ''' Copy the screen-buffer onto the display device. '''
        for ss, row in enumerate(self.screen_rows):
            buffer = ''
            for zch in self.screen[ss]:
                buffer += zch
            self.canvas.itemconfigure(row, text=buffer, font=self.font)

    def plot(self, ichar, cellx, celly):
        '''
        Place a character into the screen-buffer.
        Return True on success, else False.
        '''
        if cellx < self.cell_width:
            if celly < self.cell_height:
                self.screen[celly][cellx] = ichar
                return True
        return False

    def on_dump(self, event):
        zdict = event.__dict__
        for key in zdict:
            print("{0:>10s} = {1} ".format(key, zdict[key]))
        print('=' * 10)

    def event_KeyPress(self, event):
        if False:
            self.on_dump(event)
        else:
            key = event.char
            if key in self.actions:
                self.actions[key][2](self.view)
            if self.game_over:
                self.destroy()
            else:
                self.event_gameStep()

    def event_gameStep(self):
        if self.view.do_next() is False:
            self.game_over = True
        self.view.on_plot(self)

    def on_up(self, view):
        self.view.do_up(self)

    def on_down(self, view):
        self.view.do_down(self)

    def on_left(self, view):
        self.view.do_left(self)

    def on_right(self, view):
        self.view.do_right(self)

    def on_help(self, view):
        for key in self.actions:
            info = self.actions[key]
            print("'{}' = {}".format(info[0], info[1]))
        input(" --- enter ---")

    def on_quit(self, view):
        self.game_over = True

    def on_start(self, view):
        self.view = view
        print("on_start")
        self.start()

    def on_jump(self, view):
        self.view = view
        print("on_jump")
    
    def mainloop(self, view):
        self.on_start(view)

