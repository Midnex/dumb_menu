import os
import re
try:
    import curses
except ModuleNotFoundError:
    if os.name == "nt":
        print("Please install windows-curses")

class Menu:
    def __init__(self, options, title):
        self.options = options
        self.selected_index = 0
        self.title = title

    def __del__(self):
        curses.endwin()

    def get_menu_choice(self, screen):
        key_up = 450 if os.name == "nt" else 259
        key_down = 456 if os.name == "nt" else 258
        key_esc = 27
        key_enter = 10

        while True:
            self.show_menu(screen)
            key = screen.getch()
            if key == key_esc:
                self.selected_index = -1
                return self.selected_index
            elif key == key_enter:
                return self.selected_index
            elif key == key_up:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif key == key_down:
                self.selected_index = (self.selected_index + 1) % len(self.options)

    def show_menu(self, screen):
        screen.clear()
        screen.addstr(f"{self.title}\n", curses.A_BOLD)
        index = 1
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                screen.addstr(f"> {index}. {option}\n", curses.A_REVERSE)
            else:
                screen.addstr(f"  {index}. {option}\n")
            index += 1
        screen.addstr("\nUse the arrow keys to move and Enter to select.")

    def show(self, screen):
        index = self.get_menu_choice(screen)

        if index != -1:
            screen.clear()
            # screen.addstr(f"You selected option {index + 1}: {self.options[index]}")
            # screen.refresh()
            # screen.getch()
            return index
        else:
            screen.clear()
            screen.addstr("You exited the menu.")
            screen.refresh()
            screen.getch()
            return 0

def demo(screen):
    options = ["Abc", "123", "!@#"]
    menu = Menu(options, title="Select Something")

    screen.clear()
    index = menu.show(screen)
    screen.addstr(index)
    screen.refresh()
    screen.getch()
    input()

if __name__ == "__main__":
    curses.wrapper(demo)