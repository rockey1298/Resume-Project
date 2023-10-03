from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import settings
import utils
import login_buttons


root = Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("All Breed Dog Grooming")
root.resizable(False, False)
# root.attributes("-fullscreen", True)

# white header background
top_frame = Frame(root, bg="white", width=settings.WIDTH, height=utils.height_prct(10))
top_frame.place(x=0, y=0)


# pink testing button thing
header = Label(top_frame, bg="pink", text="ALL BREED DOG GROOMING", font=("", 24))
header.place(x=utils.width_prct(25), y=0)

# purple boi
login_frame = Frame(
    root, bg="purple", width=utils.width_prct(33), height=utils.height_prct(75)
)
login_frame.place(x=utils.width_prct(33), y=utils.height_prct(10))

# login buttons
login_btn_frame = Frame(
    root, bg="orange", width=utils.width_prct(16.5), height=utils.height_prct(15)
)
login_btn_frame.place(x=utils.width_prct(41.25), y=utils.height_prct(60))
# button tutorial

# Creates top frame
frame1 = LabelFrame(root, width=400, height=180, bd=5, bg="white")
frame1.pack()

# Stop the frame from propagating the widget to be shrink or fit
frame1.pack_propagate(False)
# Trying to place the frame
# frame1.place

# Create an Entry widget in Frame1
entry1 = ttk.Entry(frame1, width=40)
entry1.insert(INSERT, "Enter Your Name")
entry1.pack(pady=30)
entry2 = ttk.Entry(frame1, width=40)
entry2.insert(INSERT, "Enter Your Email")
entry2.pack()

# Creates bottom frame for button
frame2 = LabelFrame(root, width=150, height=100)
frame2.pack()

# Create a Button to enable frame
button1 = ttk.Button(frame2, text="Submit", command=utils.submit)
button1.pack()

root.mainloop()
