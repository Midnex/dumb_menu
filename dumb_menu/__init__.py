import os
import re

#region windows
def get_menu_choice1(options):
    shortcuts = scan_short_cuts(options) # scan for shortcuts
    selectedIndex = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear") #clear screen
        show_menu(options,selectedIndex)

        key = b"\a" #default to error
        try:
            import msvcrt
            char = msvcrt.getch() #get keypress
        except :
            pass

        if key == b"\x1b":  # Esc key to exit # doesn't work on linux
            return -1
        elif key == b"\r":  # Enter key to select
            return selectedIndex
        elif key in (b"\x48", b"\x50"):  # Up or Down arrow
            selectedIndex = (selectedIndex + (1 if key == b"\x50" else -1) + len(options)) % len(options)
        elif key in shortcuts: # Shortcut key
            return shortcuts[key]
        elif key == b"\a":
            print("error , may not support your system")
            exit()

# endregion
def get_key(): #get keypress using getch, msvcrt = windows
    flag_have_getch = False
    flag_have_msvcrt = False
    try :
        import getch
        flag_have_getch = True
        first_char = getch.getch()
        if first_char == "\x1b": #arrow keys
            a=getch.getch()
            print(a)
            b=getch.getch()
            print(b)
            return {"[A": "up", "[B": "down", "[C": "right", "[D": "left" }[a+b]
        if ord(first_char) == 10:
            return  "enter"
        if ord(first_char) == 32:
            return  "space"
        else:
            return first_char #normal keys like abcd 1234
    except :
        pass
    
    try:
        import msvcrt
        flag_have_msvcrt = True
        key = msvcrt.getch()  # get keypress
        if key == b"\x1b":  # Esc key to exit
            return "esc"
        elif key == b"\r":  # Enter key to select
            return "enter"
        elif key == b"\x48":  # Up or Down arrow
            return  "up"
        elif key == b"\x50":  # Up or Down arrow
            return "down"
        else:
            return key.decode("utf-8")
    except:
        pass


def get_menu_choice(options, title=None, isClean = False):
    """ Selection for menu item"""
    shortcuts = scan_short_cuts(options)  # scan for shortcuts
    selectedIndex = 0
    # print(shortcuts) # does this do anything?
    while True:
        show_menu(options, title, selectedIndex, isClean)
        key = get_key()
        if key == "enter":  # Enter key to select
            return selectedIndex
        elif key in ("up","down"):  # Up or Down arrow
            selectedIndex = (selectedIndex + (1 if key == "down" else -1) + len(options)) % len(options)
        elif key in shortcuts:  # Shortcut key
            show_menu(options, title, shortcuts[key],isClean) #show selected option when using shortcut
            return shortcuts[key]

def scan_short_cuts(options):
    """ Checks for shortcuts, must be encased in brackets. [1]/[a] """
    shortcuts = {}
    for i, option in enumerate(options):
        match = re.match(r"\[(.*)\](.*)", option)
        if match:
            shortcut, _ = match.group(1, 2)
            shortcuts[shortcut] = i
    return shortcuts

def show_menu(options, title, selectedIndex, isClean):
    """ Shows menu with a foot, or without"""
    if isClean:
        show_clean_menu(options, title, selectedIndex)
    else:
        show_normal_menu(options, title, selectedIndex)


def show_normal_menu(options, title, selectedIndex):
    """ shows menu """
    os.system("cls" if os.name == "nt" else "clear")
    print(title)
    for i, option in enumerate(options):
        if i == selectedIndex:
            print(f"> {option}")
        else:
            print(f"  {option}")
    print("\nUse the arrow keys to move, Enter/Hotkey to select.")

def show_clean_menu(options, title, selectedIndex):
    """ Shows menu without bottom footer. """
    os.system("cls" if os.name == "nt" else "clear")
    print(title)
    for i, option in enumerate(options):
        if i == selectedIndex:
            print(f"> {option}")
        else:
            print(f"  {option}")

def demo():
    options = ["[1]Option 1", "[2]Option 2", "[3]Option 3","[q]quit"]
    index = get_menu_choice(options,title="This is a Demo Title", isClean=False)

    if index != -1:
        print(f"You selected option {index + 1}: {options[index]}")
    else:
        print("You exited the menu.")

# # test code 
# if __name__ == "__main__":
#     demo()