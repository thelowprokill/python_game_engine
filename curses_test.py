#!/usr/bin/env python3

from curses import wrapper
import curses

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.nodelay(True)

    run   = True
    frame = 0

    x = 0
    y = 2

    #while run:
    #    stdscr.clear()
    #    
    #    buffer = []
    #    c = stdscr.getch()
    #    while c != curses.ERR:
    #        buffer.append(c)
    #        c = stdscr.getch()

    #    print(f"Buffer: {buffer}")

    #    for c in buffer:
    #        stdscr.addstr(y, 0, str(c))
    #        y += 1

    #    stdscr.refresh()
    #    frame += 1
    #for c in buffer:
    #    if c != curses.ERR:
    #        if c == ord('q'):
    #            run = False
    #        if c == ord('w'):
    #            y -= 1
    #        if c == ord('s'):
    #            y += 1
    #        if c == ord('a'):
    #            x -= 1
    #        if c == ord('d'):
    #            x += 1


    while run:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Hello, World! {frame}")
        stdscr.addstr(1, 0, str(curses.has_colors()))
        stdscr.addstr(y, x, "Should be red!", curses.color_pair(1))

        stdscr.refresh()

        frame += 1

        buffer = []

        c = stdscr.getch()
        while c != curses.ERR:
            buffer.append(c)
            c = stdscr.getch()

        print(f"Buffer: {buffer}")

        for c in buffer:
            if c != curses.ERR:
                if c == ord('q'):
                    run = False
                if c == ord('w'):
                    y -= 1
                if c == ord('s'):
                    y += 1
                if c == ord('a'):
                    x -= 1
                if c == ord('d'):
                    x += 1


wrapper(main)
