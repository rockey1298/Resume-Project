import tkinter as tk
import parent_class as pt

root = tk.Tk()
root.title("Main page - using objects with tkinter")
root.geometry("800x600")


class Elder:
    counter = 0

    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.pack()

        self.myButton = tk.Button(master, text="Swag big", command=self.fncSwagBig)
        self.myButton.pack(pady=20)

    def fncSwagBig(self):
        print("big clicker bud")


e = Elder(root)
p = pt.Parent(e)
root.mainloop()
