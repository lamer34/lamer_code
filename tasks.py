import pyautogui
import numpy

moduls = ["pyautogui", "numpy"]


def scroll_mouse():
    pyautogui.moveTo(100, 200)


def scroll_again():
    pyautogui.moveTo(500, 100)


def write_numbers():
    print(numpy.arange(10))


def any_func():
    pass


def main():
    scroll_mouse()
    scroll_again()
    write_numbers()
    any_func()

if __name__ == "__main__":
    main()
