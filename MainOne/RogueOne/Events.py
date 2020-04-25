#!/usr/bin/env python3

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../'))

from RogueOne.Points import *
from tkinter import *

class EventGUI(Tk):
    
    ''' The TK window that we use for drawing, as well as managing input events. '''

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
        ''' One can call either start(), or mainloop(below), but not both '''
        self.view = view
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.bind_all('<Home>', self.event_NavPress, '+')
        self.bind_all('<End>', self.event_NavPress, '+')
        self.bind_all('<Return>', self.event_NavPress, '+')
        self.bind_all('<Insert>', self.event_NavPress, '+')
        self.bind_all('<Delete>', self.event_NavPress, '+')
        self.bind_all('<Prior>', self.event_NavPress, '+') # Page Up
        self.bind_all('<Next>', self.event_NavPress, '+')  # Page Down
        self.bind_all('<Print>', self.event_NavPress, '+')
        self.bind_all('<BackSpace>', self.event_NavPress, '+')
        self.bind_all('<Tab>', self.event_NavPress, '+')

        self.bind_all('<F1>', self.event_NavPress, '+')
        self.bind_all('<F2>', self.event_NavPress, '+')
        self.bind_all('<F3>', self.event_NavPress, '+')
        self.bind_all('<F4>', self.event_NavPress, '+')
        self.bind_all('<F5>', self.event_NavPress, '+')
        self.bind_all('<F6>', self.event_NavPress, '+')
        self.bind_all('<F7>', self.event_NavPress, '+')
        self.bind_all('<F8>', self.event_NavPress, '+')
        self.bind_all('<F9>', self.event_NavPress, '+')
        self.bind_all('<F10>', self.event_NavPress, '+')
        self.bind_all('<F11>', self.event_NavPress, '+')
        self.bind_all('<F12>', self.event_NavPress, '+')

        self.bind_all('<Up>', self.event_NavPress, '+')
        self.bind_all('<Down>', self.event_NavPress, '+')
        self.bind_all('<Left>', self.event_NavPress, '+')
        self.bind_all('<Right>', self.event_NavPress, '+')
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
        ''' When your UI is no longer needed, use stop() to close the window. '''
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

    def grid2gui(self, gridPoint):
        xpos = ((gridPoint.x + 1) * self.font_sz)
        if sys.platform[0] == 'w':
            xpos -= (gridPoint.x * 3) # Windows 10 ... + other 'dozes?
        ypos = gridPoint.y + 1
        return GuiPoint(xpos, ypos * self.font_sz)

    def peek(self, gridPoint):
        '''
        Return a character from the screen-buffer. Return 'None' if the point
        was invalid.
        '''
        if gridPoint.x < self.cell_width:
            if gridPoint.y < self.cell_height:
                return self.screen[gridPoint.y][gridPoint.x]
        return None

    def plot(self, ichar, gridPoint):
        '''
        Place a character into the screen-buffer.
        Return True on success, else False.
        '''
        if gridPoint.x < self.cell_width:
            if gridPoint.y < self.cell_height:
                self.screen[gridPoint.y][gridPoint.x] = ichar
                return True
        return False

    def event_Dump(self, event):
        ''' A handy way to see what a Tkinter Event has to offer. '''
        zdict = event.__dict__
        for key in zdict:
            print("{0:>10s} = {1} ".format(key, zdict[key]))
        print('=' * 10)
    
    def event_MouseClick(self, event):
        ''' Used by the event manager. Also handy for injecting test cases. '''
        self.view.event_MouseClick(event.num, event.x_root, event.y_root)
    
    def event_KeyPress(self, event):
        ''' Used by the event manager. Also handy for injecting test cases. '''
        self.view.event_KeyPress(event.char, event.x_root, event.y_root)
    
    def event_NavPress(self, event):
        ''' Used by the event manager. Also handy for injecting test cases. '''
        self.view.event_KeyPress(event.keysym, event.x_root, event.y_root)
        
    def mainloop(self, view):
        ''' One can call either start(above), or mainloop(), but not both '''
        self.start(view)

