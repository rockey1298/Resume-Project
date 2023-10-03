from tkinter import Button


class my_button:
    def __init__(self):
        self.sneaky_button = None
        pass

    def create_btn_object(self, location):
        btn = Button(location, width=12, height=4)
        btn.bind("<Button-1>", self.left_click_actions)
        self.sneaky_button = btn
