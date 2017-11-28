import curses

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
curses.mousemask(curses.ALL_MOUSE_EVENTS)

screen.addstr("This is a Sample Curses Script\n\n")
x = 3
while True:
    event = screen.getch()
    if event == ord("q"): break
    if event == curses.KEY_MOUSE:
        _, mx, my, _, mstate = curses.getmouse()
        if mstate == curses.BUTTON3_PRESSED:
            screen.addstr(x,0, "!" + str(mstate) + "!")
        else:
            screen.addstr(x,0, str(mstate))
        x += 1
    #     y, x = screen.getyx()
    #     screen.addstr(3, 0, "pressed @ (" + str(mx) + ", " + str(my) + ")")

curses.endwin()
