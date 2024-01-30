import curses
import os

key_up = 450 if os.name == "nt" else 259
key_down = 456 if os.name == "nt" else 258

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr("Press up/down arrow keys. Press q to quit.\n")
    while (key := stdscr.getch()) != ord('q'):
        stdscr.addstr("Up\n" if key == key_up else "Down\n" if key == key_down else "")

if __name__ == '__main__':
    curses.wrapper(main)