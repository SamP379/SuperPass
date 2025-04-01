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



def create_logged_out_page(self):
        """Creates the UI components for the logged-out state, including login and register frames."""

        # Create the logged out frame
        self.logged_out_frame = Frame(self.window, bg = "#030621", highlightthickness = 0)

        # Create the register frame
        self.register_frame = Frame(self.logged_out_frame, bg = "#030621")
        self.register_button = Button(self.register_frame, text = "Register", height = 2, command = self.register_user) 
        self.register_button.grid(row = 0, column = 0)
        self.register_entry = Entry(self.register_frame, width = 30, font = ('Arial', 15)) 
        self.register_entry.grid(row = 0, column = 1, padx = 10)
        self.register_frame.grid(row = 0, column = 0, pady = 15)

        # Create the login frame
        self.login_frame = Frame(self.logged_out_frame, bg = "#030621")
        self.login_button = Button(self.login_frame, text = "Login", width = 6, height = 2, command = self.login_user) 
        self.login_button.grid(row = 0, column = 0)
        self.login_entry = Entry(self.login_frame, width = 30, font = ('Arial', 15)) 
        self.login_entry.grid(row = 0, column = 1, padx = 10)
        self.login_frame.grid(row = 1, column = 0)



def create_logged_in_page(self):
        """Creates the UI components for the logged-in state, including options and account details frames."""

        # Create the options frame
        self.options_frame = Frame(self.window, bg = "#030621", highlightthickness = 0)
        self.search_button = Button(self.options_frame, text = "Search", width = 10, height = 2, command = self.search_website)
        self.search_button.grid(row = 0, column = 0, padx = 23)
        self.add_button = Button(self.options_frame, text = "Add", width = 10, height = 2, command = self.add_website)
        self.add_button.grid(row = 0, column = 1, padx = 23)
        self.websites_button = Button(self.options_frame, text = "Websites", width = 10, height = 2, command = self.view_websites)
        self.websites_button.grid(row = 0, column = 2, padx = 23)

        # Create the account details frame
        self.account_details_frame = Frame(self.window, bg = "#030621", highlightthickness = 0)
        self.website_label = Label(self.account_details_frame, text = "Website", width = 8)
        self.website_label.grid(row = 0, column = 0, padx = (0,20), pady = 5)
        self.website_entry = Entry(self.account_details_frame, width = 30)
        self.website_entry.grid(row = 0, column = 1)
        self.username_label = Label(self.account_details_frame, text = "Username", width = 8)
        self.username_label.grid(row = 1, column = 0, padx = (0,20), pady = 5)
        self.username_entry = Entry(self.account_details_frame, width = 30)
        self.username_entry.grid(row = 1, column = 1)
        self.email_label = Label(self.account_details_frame, text = "Email", width = 8)
        self.email_label.grid(row = 2, column = 0, padx = (0,20), pady = 5)
        self.email_entry = Entry(self.account_details_frame, width = 30)
        self.email_entry.grid(row = 2, column = 1)
        self.password_label = Label(self.account_details_frame, text = "Password", width = 8)
        self.password_label.grid(row = 3, column = 0, padx = (0,20), pady = 5)
        self.password_entry = Entry(self.account_details_frame, width = 30)
        self.password_entry.grid(row = 3, column = 1)



def update_ui(self):
        """Updates the UI based on the login state, showing either the logged-out or logged-in view."""
        if not self.is_logged_in:
            self.login_entry.focus()
            self.logged_out_frame.grid(row = 1, column = 0, pady=(0,20))
        else:
            self.logged_out_frame.grid_forget()
            self.website_entry.focus()
            self.options_frame.grid(row = 1, column = 0)
            self.account_details_frame.grid(row = 2, column = 0, pady=(30,20))



def register_user(self):
        """Fetches the entered password and calls the manager to handle registration"""
        password = self.register_entry.get()
        if len(password) == 0:
            messagebox.showinfo(title = "Oops", message = "Enter the master password before registering.")
        else:
            if self.manager.handle_registration(password):
                messagebox.showinfo(title = "Success", message = "Registration was successful!")
            else:
                messagebox.showinfo(title = "Oops", message = "You have already registered.")



def login_user(self):
        """Fetches the entered password and calls the manager to handle login."""
        login_password = self.login_entry.get()
        if self.manager.handle_login(login_password):
            self.is_logged_in = True
            self.update_ui()
        else:
            messagebox.showinfo(title = "Oops", message = "Log in unsuccessful.")