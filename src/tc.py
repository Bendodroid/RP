# Terminal-Convenience-functions


import os
import sys


def clear_term():
    """Clears the terminal"""
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def create_header(text: str, clearterm: bool=True):
    """Creates a header"""
    if clearterm is True:
        clear_term()
    try:
        width = os.get_terminal_size()[0]
    except OSError:
        width = 120
    borders = ""
    borders += width * "~"
    width -= len(text)
    spaces = width // 2
    space = ""
    space += spaces * " "
    print(borders)
    print("\n" + space + text)
    print("\n" + borders)
    print("\n\n")


def align_string(string: str, position: int=5):
    """Aligns a string"""
    try:
        alignindent = (os.get_terminal_size()[0] // position)
    except OSError:
        alignindent = 50
    spaces = (alignindent - len(string)) * " "
    return str(spaces + string)


def set_term_title(msg: str):
    if os.name == "posix":
        sys.stdout.write("\x1b]2;%s\x07" % msg)
        return True
    elif os.name == "nt":
        return False


def print_warning(msg: str):
    print("\n   [WARNING]   " + msg + "\n")


def print_message(msg: str, label: str):
    return str("\n   [" + label + "] " + msg + "\n")


def create_infobox(msg: str, border: str="~", position: int=5, clearterm: bool=False):
    if clearterm is True:
        clear_term()
    try:
        indent = (os.get_terminal_size()[0] // position)
    except OSError:
        indent = 50
    lspace = (indent - len(msg)) * " "
    upborder = (len(msg) + 12) * border
    mid = border + (5 * " ") + msg + (5 * " ") + border
    print(lspace + upborder)
    print(lspace + mid)
    print(lspace + upborder)
