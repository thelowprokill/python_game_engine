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

        #self.objects = []
        #self.input_handler = InputHandler()

    #def add_object(self, obj):
    #    self.objects.append(obj)

    #def tick(self, dt):
    #    #c = self.input_handler.get_input()
    #    for o in self.objects:
    #    #    o.input(c)
    #        o.tick(dt)

    #    self.draw()

#    def draw(self, objects):
#        for y in range(self.height):
#            for x in range(self.width):
#                char = " "
#                z_index = 0
#                c_color = None
#                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
#                    char = "="
#                else:
#                    for obj in objects:
#                        c, z, color = obj.draw(x, y)
#                        if c != "" and z >= z_index:
#                            char = c
#                            z = z_index
#
#                if c_color is not None:
#                    char = f"{c_color}{char}\033[0m"
#
#                print(char, end="")
#            print("")


    def draw(self, objects):
        self.window.clear()

        # draw border
        top = ""
        for i in range(self.width):
            top += "="

        self.window.addstr(0, 0, top)
        self.window.addstr(self.height - 1, 0, top)
        for i in range(1, self.height - 1):
            self.window.addstr(i, 0, "|")
            self.window.addstr(i, self.width - 1, "|")
            
        # draw objects
        for obj in objects:
            obj.render(self.window)

        self.window.refresh()
