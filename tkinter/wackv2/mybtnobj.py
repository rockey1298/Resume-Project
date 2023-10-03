import tkinter as TKTK


class myBtnObj:
    btn_list = []

    def __init__(self, fn, btnbool, root, clblf, cen_cust_frame):
        self.customer_frame = cen_cust_frame
        self.customer_label_frame = clblf
        self.root = root
        self.firstname = fn
        self.isbtn = btnbool
        self.isbtn = True
        print("printing my btn list ! ")
        print(myBtnObj.btn_list)
        # print(type(self.firstname))
        if self.isbtn == True:
            self.fncMakeCustBtn()

    def get_customer_labelframe():
        pass

    def fncMakeCustBtn(self):
        # i = 3
        customer_button = TKTK.Button(
            self.customer_label_frame,
            text=self.firstname,
            command=self.fncChangingCenterFrame,
        )
        myBtnObj.btn_list.append(customer_button)
        # customer_button.grid(row=1, column=i)
        # for obj in myBtnObj.btn_list:
        #     obj.grid(row=0, column=i)
        #     i += 2

    def fncCustomerRefresh1():
        print("Customer refresh function!")
        i = 3
        for obj in myBtnObj.btn_list:
            obj.grid(row=0, column=i)
            i += 2

    def fncChangingCenterFrame(self):
        self.customer_information_frame = TKTK.Frame(
            self.customer_frame, bg="yellow", height=300, width=300
        )
        self.customer_information_frame.place(x=50, y=50)
        self.customer_information_label = TKTK.Label(
            self.customer_information_frame, text="hello" + self.firstname
        )
        self.customer_information_label.place(x=0, y=0)
