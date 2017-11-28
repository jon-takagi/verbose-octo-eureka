import curses
class Window():
    def __init__(self):
        self.scr = curses.initscr()
        self.scr.keypad(1)
        curses.mousemask(curses.ALL_MOUSE_EVENTS)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, 255)
        self.scr.bkgd(" ", curses.color_pair(0))
