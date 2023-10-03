import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    t = term_status_var.get()
    if t == "Accepted":

        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:

            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            print(f"First name: {firstname}, Lastname: {lastname}")
            print(f"Title: {title}, age: {age}, nationality: {nationality}")

            # Course info
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            registration_status = reg_status_var.get()
            term_status = term_status_var.get()

            print(f"# courses: {numcourses}, # semesters {numsemesters}")
            print(f"registration status : {registration_status}")
            print(f"Terms :{term_status}")
            print("-------------------------")
        else:
            tkinter.messagebox.showwarning(
                title="Error", message="First and last name are required "
            )
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="You have not accepted the terms"
        )


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


age_label = tkinter.Label(user_info_frame, text="age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="nationality")
nationality_combobox = ttk.Combobox(
    user_info_frame,
    values=["africa", "antarctica", "asia", "europe", "north america", "south america"],
)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# second frame
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_label.grid(row=0, column=0)


# value holding checkbutton status
reg_status_var = tkinter.StringVar(value="Not registered")


registered_check = tkinter.Checkbutton(
    courses_frame,
    text="currently registered",
    variable=reg_status_var,
    onvalue="registered",
    offvalue="not registered",
)


registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# of completed courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")

numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")

numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# terms checkbox
term_status_var = tkinter.StringVar(value="Terms not accepted")
terms_check = tkinter.Checkbutton(
    terms_frame,
    text="I accept terms and conditions",
    variable=term_status_var,
    onvalue="Accepted",
    offvalue="Declined",
)
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
