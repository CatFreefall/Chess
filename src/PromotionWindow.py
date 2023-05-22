from tkinter import *

class PromotionWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("150x30")
        self.option = StringVar(self.window)
        self.option.set("Options")

        promotion_menu = OptionMenu(self.window, self.option, "Queen", "Rook", "Bishop", "Knight")
        promotion_menu.pack()

        self.option.trace("w", self.get_selected)

        self.selected_value = None

    def get_selected(self, *args):
        self.selected_value = self.option.get()
        self.window.destroy()

    def run(self):
        self.window.mainloop()
