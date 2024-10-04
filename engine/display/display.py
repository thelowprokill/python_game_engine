#!/usr/bin/env python3

import curses

class Display:
    def __init__(self):
        self.width   = 180
        self.height  = 50
        self.window = None

    def set_window(self, window):
        self.window = window
        curses.init_pair(1, curses.COLOR_RED,    curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE,   curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN,  curses.COLOR_BLACK)
        self.width  = curses.COLS  - 1
        self.height = curses.LINES - 1

    def draw(self, objects):
        self.window.clear()

        # draw objects
        for obj in objects:
            obj.render(self.window)

        # draw border
        top = ""
        for i in range(self.width):
            top += "="

        self.window.addstr(3, 0, top)
        self.window.addstr(self.height - 1, 0, top)
        for i in range(4, self.height - 1):
            self.window.addstr(i, 0, "|")
            self.window.addstr(i, self.width - 1, "|")
            

        self.window.refresh()
