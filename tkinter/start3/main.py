import tkinter as tk
import utils
from customer import customer


# global customer_entry_labelframe
# checking user input for login field then forgetting login frame and packing user frame.


def fncChecklogin():
    username = login_frame_username_register_field.get()
    password = login_frame_label_password_register_field.get()
    print(f"User and password: {username}{password}")
    if username == "" and password == "":
        login_frame.pack_forget()
        user_frame.pack()
        print("login frame to user frame")


# when you go between frames you are manually calling them instead of
# having a more streamlined way so you can scale properly
def fncNewCustomer():
    print("hello world")
    print("~~~~~~~~~~~~")

    fncClearCenterFrame()
    customer_entry_labelframe.pack()


def fncCalander():
    print("Hello calander")
    print("~~~~~~~~~~~~~~~~")
    fncClearCenterFrame()
    calander_frame.pack()


def fncClearCenterFrame():
    for child in center_frame.winfo_children():
        child.pack_forget()


def fncCustomerSubmit(sidebar_customer_frame):
    print("Customer submit button pressed!")
    customerFirstName = customer_entry_register_field.get()
    print(customerFirstName)
    Mycustomer = customer(customerFirstName, sidebar_customer_frame)
    # for c in customer.customer_list:
    #     print(c.name)

    # def fncCustomerRefresh(sidebar_customer_frame):
    #     i = 1
    #     for c in customer.customer_list:
    #         c = tk.Button(
    #             sidebar_customer_frame,
    #             text=c.name,
    #             command=c.fncShowCustomerPanel,
    #         )
    #         c.grid(row=i, column=0)
    #         i += 1

    for c in customer.customer_list:
        print(c.name)
    print("~~~~~~~~~~~")


# def fncShowCustomerPanel(self):
#     pass


root = tk.Tk()
root.title("creating multiple pages")
root.geometry("1920x1080")
# root.configure(bg="orange")

# grey first login frame!


login_frame = tk.Frame(root, bg="grey")
login_frame.grid(row=0, column=0, padx=20, pady=10)

login_frame_label_username = tk.Label(login_frame, text="Username", bg="grey")
login_frame_username_register_field = tk.Entry(login_frame)

login_frame_label_username.grid(row=0, column=0)
login_frame_username_register_field.grid(row=0, column=1)

login_frame_label_password = tk.Label(login_frame, text="Password", bg="grey")
login_frame_label_password.grid(row=1, column=0)

login_frame_label_password_register_field = tk.Entry(login_frame)
login_frame_label_password_register_field.grid(row=1, column=1)

login_submit_button = tk.Button(
    login_frame,
    text="submit",
    command=fncChecklogin,
)
login_submit_button.grid(row=3, column=0, columnspan=2, sticky="news")

for widget in login_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

login_frame.pack()
login_frame.place(x=900, y=300)


# user frame , what user sees after logging in , base frame


user_frame = tk.Frame(root, bg="white", height=1080, width=1920)

# navbar frame

navbar_frame = tk.Frame(
    user_frame, bg="grey", height=utils.height_prct(10), width=utils.width_prct(100)
)
navbar_frame.place(x=0, y=0)


# creating a grid frame to hold buttons in navbar


navbar_nav_btn_list = tk.Frame(
    navbar_frame, bg="orange", height=utils.height_prct(10), width=utils.width_prct(100)
)
navbar_nav_btn_list.place(x=0, y=0)


# Buttons in navbar grid, but they are being placed. idk


btn_create_customer = tk.Button(
    navbar_nav_btn_list, text="New customer", command=fncNewCustomer
)
btn_create_customer.place(x=utils.width_prct(15), y=utils.height_prct(7))

btn_calender = tk.Button(
    navbar_nav_btn_list,
    text="Calender",
    command=fncCalander,
)
btn_calender.place(x=utils.width_prct(20), y=utils.height_prct(7))

btn_clear_center = tk.Button(
    navbar_nav_btn_list, text="CLEAR", command=fncClearCenterFrame
)
btn_clear_center.place(x=utils.width_prct(25), y=utils.height_prct(7))

# side bar frame


sidebar_frame = tk.Frame(
    user_frame, bg="pink", height=utils.height_prct(90), width=utils.width_prct(15)
)
sidebar_frame.place(x=0, y=utils.height_prct(10))


# within the sidebar , we need to have the list of customers !
# lets create a place for them to go , then we will figure out how to display a list


sidebar_customer_frame = tk.LabelFrame(
    sidebar_frame,
    bg="purple",
    height=utils.height_prct(10),
    width=utils.width_prct(10),
    text="storing customers here!",
)
sidebar_customer_frame.grid(row=0, column=0)

sidebar_customer_label = tk.Label(
    sidebar_customer_frame,
    text=" Here are the customers!",
)
sidebar_customer_label.grid(row=0, column=0)

Mycustomer = customer("ADMIN", sidebar_customer_frame)
# CENTER FRAME IN USER FRAME


center_frame = tk.Frame(
    user_frame, bg="yellow", height=utils.height_prct(90), width=utils.width_prct(85)
)
center_frame.place(x=utils.width_prct(15), y=utils.height_prct(10))


# Customer entry label frame, happens at start not sure why and is the base frame
# for the customer entry grid


customer_entry_labelframe = tk.LabelFrame(center_frame, text="New Customer")
customer_entry_labelframe.grid(
    row=0,
    column=0,
)
customer_entry_label = tk.Label(customer_entry_labelframe, text="First name :")
customer_entry_label.grid(row=0, column=0)

customer_entry_register_field = tk.Entry(customer_entry_labelframe)
customer_entry_register_field.grid(row=0, column=1)

customer_submitbutton = tk.Button(
    customer_entry_labelframe,
    text="submit",
    command=lambda: fncCustomerSubmit(sidebar_customer_frame),
)
customer_submitbutton.grid(row=0, column=2)

customer_refreshbutton = tk.Button(
    customer_entry_labelframe,
    text="Refresh button!",
    command=lambda: customer.fncShowCustomerPanel(sidebar_customer_frame),
)
customer_refreshbutton.grid(row=0, column=3)

# creating the frame you will see when you click on the customer button


# calander frame


calander_frame = tk.Frame(
    center_frame, bg="red", height=utils.height_prct(90), width=utils.width_prct(85)
)
calander_frame.place(x=0, y=0)

root.mainloop()
