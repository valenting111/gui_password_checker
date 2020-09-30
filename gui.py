from tabnanny import check
from tkinter import *
from password_checker import *

class CustomGui():
    def __init__(self):
        self.my_window = Tk()
        self.my_window.title("Password Checker")
        self.label1 = Label(self.my_window, text="Let's verify the strength of your password. \n"
                                                 "To be strong it should contain at least 8 characters, of which at "
                                                 "least: "
                                                 "\n "
                                                 "An uppercase letter. \n"
                                                 "An lowercase letter. \n"
                                                 "A digit. \n"
                                                 "A special character from @$!%*#?& \n",
                            bg="white", fg="black", font="none 12 bold", )
        self.label1.config(anchor=CENTER)

        self.label2 = Label(self.my_window, text="Password:", fg="black", font="none 12 bold")
        self.label2.config(anchor=CENTER)

        self.widget1 = Entry(self.my_window, {"show": "*"})
        self.button1 = Button(self.my_window, {"text": "Reset password", "command": self.reset_pwd})
        self.button2 = Button(self.my_window, {"text": "Submit", "command": self.check_pwd_valid})

        self.label1.pack()
        self.label2.pack()
        self.widget1.pack()
        self.button2.pack()
        self.button1.pack()

    def reset_pwd(self):
        self.widget1.delete(0, "end")
        self.label2.config(text="Password:", fg="black")

    def check_pwd_valid(self):
        if check_valid(self.widget1.get()):
            self.label2.config(text="Strong enough", fg="green")
        else:
            self.label2.config(text="Not strong enough", fg="red")

    def show_gui(self):
        self.my_window.mainloop()
