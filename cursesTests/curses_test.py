import curses

scr = curses.initscr()
curses.noecho()
curses.curs_set(0)
scr.keypad(1)
curses.mousemask(curses.ALL_MOUSE_EVENTS)

scr.addstr("This is a Sample Curses Script\n\n")

while True:
    curses.echo()
    command = scr.getstr(2, 0, 11)
    curses.noecho()
    scr.addstr(3, 0, command)
    scr.addstr(2, 0, " "*11)
curses.endwin()
