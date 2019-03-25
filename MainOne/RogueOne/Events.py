#!/usr/bin/env python3

from collections import OrderedDict
from tkinter import *
        

class EventGUI(Tk):
    
    ''' The TK window that we will use for drawing, as well as managing input events. '''

    def __init__(self, width=800, height=600):
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

    def start(self, view):
        self.view = view
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.bind_all('<KeyPress>', self.event_KeyPress, '+')
        self.bind_all('<Button-1>', self.event_MouseClick, '+')
        self.bind_all('<Button-2>', self.event_MouseClick, '+')
        self.bind_all('<Button-3>', self.event_MouseClick, '+')
        self.canvas.pack()
        self.clear_screen()
        self.font = ("Courier", self.font_sz, "bold")
        self.view.set_Parent(self)
        super().mainloop()

    def stop(self):
        self.destroy()

    def clear_screen(self):
        ''' Fills the internal screen-buffer with the default character. '''
        self.screen = [[' '] * self.cell_width
                       for yy in range(self.cell_height)]
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
    
    def event_MouseClick(self, event):
        self.view.event_MouseClick(event.num, event.x_root, event.y_root)
    
    def event_KeyPress(self, event):
        self.view.event_KeyPress(event.char, event.x_root, event.y_root)
        
    def mainloop(self, view):
        self.start(view)

