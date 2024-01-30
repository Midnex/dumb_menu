import os
import re

class Menu:
    def __init__(self, options, title, isClean=False):
        self.options = options
        self.title = title
        self.isClean = isClean
        self.shortcuts = {}
        self.selected_index = 0

        if os.name == "nt":
            import msvcrt
            self.get_key = lambda: msvcrt.getch()
            self.get_menu_choice = self.get_menu_choice_windows
        else:
            import getch
            self.get_key = lambda: getch.getch()
            self.get_menu_choice = self.get_menu_choice_linux

    def get_menu_choice_windows(self, options):
        while True:
            os.system("cls")
            self.show_menu(options)

            key = self.get_key()
            if key == b'\x1b':  # Esc key to exit
                return -1
            elif key == b'\r':  # Enter key to select
                return self.selected_index
            elif key in (b'\x48', b'\x50'):  # Up or Down arrow
                self.selected_index = (self.selected_index + (1 if key == b'\x50' else -1) + len(options)) % len(options)
            elif key in self.shortcuts:  # Shortcut key
                return self.shortcuts[key]
            else:
                print('error, may not support your system')
                exit()

    def get_menu_choice_linux(self, options):
        while True:
            os.system("clear")
            self.show_menu(options)

            key = self.get_key()
            print(key)
            if key == '\x1b':  # Esc key to exit
                return -1
            elif key == 'enter':  # Enter key to select
                return self.selected_index
            elif key in ('up', 'down'):  # Up or Down arrow
                self.selected_index = (self.selected_index + (1 if key == 'down' else -1) + len(options)) % len(options)
            elif key in self.shortcuts:  # Shortcut key
                self.show_menu(options, self.shortcuts[key])
                return self.shortcuts[key]

    def scan_shortcuts(self, options):
        for i, option in enumerate(options):
            match = re.match(r"\[(.*)\](.*)", option)
            if match:
                shortcut, _ = match.group(1, 2)
                self.shortcuts[shortcut.encode()] = i

    def show_menu(self, options):
        print(title)
        for i, option in enumerate(options):
            if i == self.selected_index:
                print(f"> {option}")
            else:
                print(f"  {option}")
        if self.isClean:
            print("Menu","current option:",self.selected_index) # this is part of isClean
        print("\nUse the arrow keys to move, Enter/Hotkey to select.")

    def demo(self):
        self.scan_shortcuts(options)
        index = self.get_menu_choice(options)

        if index != -1:
            print(f"You selected option {index + 1}: {options[index]}")
        else:
            print("You exited the menu.")

if __name__ == "__main__":
    title = "This Menu Stinks"
    options = ["[1]Option 1", "[2]Option 2", "[3]Option 3", "[q]quit"]
    menu = Menu(title=title, options=options, isClean=)
    menu.demo()