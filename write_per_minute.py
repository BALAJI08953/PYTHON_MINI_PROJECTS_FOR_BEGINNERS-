import curses
from curses import wrapper
def wpm_test(stdscr):
    target_text="HELLO THIS WPM TEST MACHINE AND MAKE THIS APP BALAJI BHAGIRATH BODDUCHERLA IS STUDYING AT AGM COLLEGE OF ENGINEERING IN VARUR IN HUBLI"
    current_text=[]
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()
    while True:
        key=stdscr.getkey()
        if ord.key(key)==27:
            break
        current_text.append(key)
        stdscr.clear()
        stdscr.addstr(target_text)
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("WELCOME TO THE SPEED TYPING TEST")
    stdscr.addstr("\n PRESS ANY KEY TO BEGIN:")
    stdscr.refresh()
    stdscr.getkey()
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

   
    start_screen(stdscr)
    wpm_test(stdscr)
wrapper(main)