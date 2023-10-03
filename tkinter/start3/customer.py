import tkinter as tk


class customer:
    customer_list = []
    countingrowforgrid = 1
    coutingcolforgrid = 0

    def __init__(self, name, sidebar_customer_frame):
        self.sb = sidebar_customer_frame
        self.name = name
        print("your name is :" + name)
        customer.customer_list.append(self)
        # for testing purposes , list storing all of the customer objects
        # for c in customer.customer_list:
        #     print(c.name)

    def hello(self):
        n = self.name
        print("Method call within class , your name is :" + n)

    def fncShowCustomerPanel(self):
        print("Refresh button clicked!")
        i = 1
        for custard in customer.customer_list:
            custard = tk.Button(
                custard.sb,
                text=custard.name,
                # currently, your looping through the list of customer objects
                # and placing them onto the sidebar frame using the grid down below!
                # however, the COMMAND you have currently issued is NOT what it needs
                # to be ! you should make NEW FUNCTION for the new customer buttons
                # so when they are clicked they take over the center customer frame
                # and display information about themselves.
                command=custard.fncShowCustomerPanel,
            )
            custard.grid(row=i, column=0)
            i += 1
        print("fncshowcustomer panel print call :")

    # Function to remove ALL children of a yet to be found parent so we can
    # have a blank slate for whatever
    # located in main file
