import pyperclip
from tkinter import *
from tkinter import messagebox
from password_manager import PasswordManager



class SuperPass():
    """
    A GUI-based password manager application that allows users to register, log in, 
    search, add, and view websites with associated account details. It manages the 
    user interface using Tkinter and handles password management tasks through 
    the PasswordManager class.
    """



    def __init__(self):

        self.is_logged_in = False
        self.manager = PasswordManager()

        # Create the main window
        self.window = Tk()
        self.window.title("SuperPass")
        self.window.configure(padx = 50, bg = "#030621")

        # Create the logo image
        logo_img = PhotoImage(file = "images/logo.png")
        self.canvas = Canvas(self.window, width = 485, height = 370, bg = "#030621", highlightthickness=0)
        self.canvas.create_image(242, 185, image = logo_img)
        self.canvas.grid(row = 0, column = 0)

        # Create the the UI pages
        self.create_logged_out_page()
        self.create_logged_in_page()

        self.update_ui()
        self.window.mainloop()