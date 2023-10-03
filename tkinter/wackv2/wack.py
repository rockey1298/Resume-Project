from functools import partial
import tkinter as tk
from mybtnobj import myBtnObj as b

root = tk.Tk()
root.title("Main page - here we go ")
root.geometry("600x600")


class Elder:
    # gets login entry fields, if they are both none then loginframe will get replaced and
    # big juicer will be displayed
    def fncCheckLogin123(self, lo, la, master):
        self.username = lo.get()
        self.password = la.get()

        print(f"User and password: {self.username},{self.password}")
        if self.username == "" and self.password == "":
            self.login_frame.place_forget()
            self.BIGJUICER(master)

    def fncCustomerSubmit(self, user_entry):
        self.entry = user_entry.get()
        # print(self.entry)
        self.customer_list.append(self.entry)
        i = 2
        ia = 0
        isbtn = False
        for zebra in self.customer_list:
            print(zebra)

            ia = b(zebra, isbtn, root, self.customer_labelframe, self.customer_frame)

            # print(zebra)
            # self.customer_button = tk.Button(
            #     self.customer_labelframe,
            #     text=f"{zebra}",
            #     command=self.fncShowCustomerFrame(zebra),
            # )
            # self.customer_button.grid(row=1, column=i)
            # self.customer_button_list.append(self.customer_button)
            # i += 1

    def fncShowCustomerFrame(self, fn):
        self.first_name = fn
        self.specific_cust = tk.Label(
            self.customer_frame, text=f"fnc show cust frame print{self.first_name}"
        )
        self.specific_cust.place_forget()
        self.specific_cust.place(x=0, y=0)

    def fncCustomerRefresh(self):
        b.fncCustomerRefresh1()

    def __init__(self, master):
        # self.wee = b()
        self.customer_list = []
        self.customer_button_list = []
        self.login_frame = tk.Frame(master, bg="orange")
        self.login_frame.grid(row=0, column=0, padx=20, pady=10)

        self.login_frame_label_username = tk.Label(
            self.login_frame, text="Username", bg="grey"
        )
        self.login_frame_username_register_field = tk.Entry(self.login_frame)

        self.login_frame_label_username.grid(row=0, column=0)
        self.login_frame_username_register_field.grid(row=0, column=1)

        self.login_frame_label_password = tk.Label(
            self.login_frame, text="Password", bg="grey"
        )
        self.login_frame_label_password.grid(row=1, column=0)

        self.login_frame_password_register_field = tk.Entry(self.login_frame)
        self.login_frame_password_register_field.grid(row=1, column=1)

        login_submit_button = tk.Button(
            self.login_frame,
            text="submit",
            command=partial(
                self.fncCheckLogin123,
                self.login_frame_username_register_field,
                self.login_frame_password_register_field,
                master,
            ),
        )
        login_submit_button.grid(row=3, column=0, columnspan=2, sticky="news")

        for widget in self.login_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.login_frame.place(x=0, y=0)

    def BIGJUICER(self, master):
        self.user_frame = tk.Frame(master, bg="black", height=200, width=600)
        self.user_frame.place(x=0, y=0)
        # bottom half of user_frame
        self.customer_frame = tk.Frame(master, bg="orange", height=400, width=600)
        self.customer_frame.place(x=0, y=200)

        self.customer_labelframe = tk.LabelFrame(self.user_frame, text="New Customer ")
        self.customer_labelframe.grid(row=0, column=0)

        self.customer_label = tk.Label(
            self.customer_labelframe, bg="brown", text="first name"
        )
        self.customer_label.grid(row=0, column=0)

        self.customer_firstname_entry = tk.Entry(self.customer_labelframe)
        self.customer_firstname_entry.grid(row=0, column=1)

        self.customer_submit_button = tk.Button(
            self.customer_labelframe,
            text="Submit",
            command=partial(self.fncCustomerSubmit, self.customer_firstname_entry),
        )
        self.customer_submit_button.grid(row=0, column=2)

        self.customer_refresh_button = tk.Button(
            self.customer_labelframe,
            text="Refresh",
            command=partial(self.fncCustomerRefresh),
        )

        for widget in self.customer_labelframe.winfo_children():
            widget.grid_configure(padx=10, pady=5)


e = Elder(root)


root.mainloop()
