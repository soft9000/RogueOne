#!/usr/bin/env python3

from collections import OrderedDict
from tkinter import *


class Event:
    ''' Add a key-level event into the loop - see set_KeyEvent(below) '''
    def __init__(self, keyChar, helpStr, on_call):
        self.keyChar = keyChar
        self.helpStr = helpStr
        self.on_call = on_call
        

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
        self.actions    = dict()
        self.set_KeyEvent(Event(char_up, "up", self.on_up))
        self.set_KeyEvent(Event(char_down, "down", self.on_down))
        self.set_KeyEvent(Event(char_left, "left", self.on_left))
        self.set_KeyEvent(Event(char_right, "right", self.on_right))
        self.set_KeyEvent(Event('?', "help", self.on_help))
        self.set_KeyEvent(Event('!', "quit", self.on_quit))

    def set_KeyEvent(self, event):
        ''' Support user-assignable, single-key, events '''
        if isinstance(event, Event) is False:
            return False
        self.actions[event.keyChar] = event
        return True

    def get_KeyEvents(self):
        return list(self.actions.keys())

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

    def event_Dump(self, event):
        zdict = event.__dict__
        for key in zdict:
            print("{0:>10s} = {1} ".format(key, zdict[key]))
        print('=' * 10)

    def event_KeyPress(self, event):
        if False:
            self.event_Dump(event)
        else:
            key = event.char
            if key in self.actions:
                action = self.actions[key].on_call
                if action:
                    action(self.view)
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
            print("'{}' = {}".format(info.keyChar, info.helpStr))

    def on_quit(self, view):
        self.game_over = True

    def on_start(self, view):
        self.view = view
        self.start()
    
    def mainloop(self, view):
        self.on_start(view)

