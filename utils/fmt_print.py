import os
import platform
class FmtPrint:
    def __init__(self):
        self.console_size = os.get_terminal_size()[0]
    def log(self, text , open = False, close = False, long = 120, little = 30, separate = False):
        if open:
            self.open_log(long)
        print(("┃"+text.center(long-2)+"┃").center(self.console_size))
        if separate:
            print(("┃"+(long-2)*"-"+"┃").center(self.console_size))
        else:
            print(("┃"+(long-2)*" "+"┃").center(self.console_size))
        if close:
            self.close_log(long)

    def open_log(self, long = 120):
        print(("┏"+(long-2)*"━"+"┓").center(self.console_size))
        print(("┃"+(long-2)*" "+"┃").center(self.console_size))
    def close_log(self, long = 120):
        print(("┗"+(long-2)*"━"+"┛").center(60).center(self.console_size))
    def clear_console(self): 
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')