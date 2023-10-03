import settings
import main
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage


def width_prct(percentage):
    return (settings.WIDTH / 100) * percentage


# Define a function to show a message
def submit():
    messagebox.showinfo("Success", +"Submitted Successfully!")
