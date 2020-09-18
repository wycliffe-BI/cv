# Brendan Ind
# cv Project user interface

import tkinter as tk


def login():
    print("Login page")


def startup():
    print("Startup")


if __name__ == "__main__":
    # On the first run we do this:
    startup()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.passwordBox = tk.Entry()
        self.usernameBox = tk.Entry()
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.login = tk.Button(self)
        self.login["text"] = "LOGIN TO\nSERVER"
        self.login["command"] = self.login
        self.login.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.passwordBox.pack()
        self.passwordBox["text"] = "Enter Password"

        self.usernameBox.pack()
        self.usernameBox["text"] = "Enter Username"
        self.usernameBox.bind("<Key-Return>", print("Hello"))

    def login(self):
        print("login to server button pressed")

    def nextBox(self, event):  # Event is arg of event to switch focus to
        event.focus_set()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
