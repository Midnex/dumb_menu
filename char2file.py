import getch


with open("char.txt", "a") as w:
    while True:
        char = getch.getch()
        byte_char = bytes(char, "utf-8")

        if char == 'q':
            break
        else:
            print(byte_char)
            w.write(f"{byte_char}\n")

