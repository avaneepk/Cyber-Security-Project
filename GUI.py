import tkinter
import string
from tkinter import messagebox

def entered_data():
    username = username_box.get()
    password = password_box.get()
    punctuation_mark = string.punctuation
    if len(username) < 2:
        tkinter.messagebox.showwarning(title = "Incorrect Username", message = "Username must have at least 2 characters.")
    if len(password) < 8:
        tkinter.messagebox.showwarning(title = "Incorrect Password", message = f"Password must have at least 8 characters which contain at least 1 number, 1 letter and 1 punctuation mark ({string.punctuation}).")
    if len(username) >= 2 and len(password) >= 8:
        count = []
        for character in password:
            if character.isdigit():
                count.append("number")
            if character in punctuation_mark:
                count.append("mark")
            if character.isalpha():
                count.append("letter")
        if "number" in count and "mark" in count and "letter" in count:
            tkinter.messagebox.showinfo(title = "Registration Status", message = "Registration Successful!")
        else:
            tkinter.messagebox.showwarning(title = "Incorrect Password", message =f"Password must have at least 8 characters which contain at least 1 number, 1 letter and 1 punctuation mark ({string.punctuation}).")
        
        #Saving account to the server.....

def authentication():
    username1 = username_box.get()
    password1 = password_box.get()
    #condition statement, connect to Server....
    tkinter.messagebox.showinfo(title = "Successful Authentication", message = f"You are authenticated! Welcome {username1}")
    #condition statement, connect to Server....
    tkinter.messagebox.showwarning(title = "Failed Authentication", message = f"Please enter correct username and password")

screen = tkinter.Tk()
screen.title("Registration Form")

frame1 = tkinter.Frame(screen)
frame1.pack()

# Signup box
signup_frame = tkinter.LabelFrame(frame1, text = "Fill in to register or authenticate an account")
signup_frame.grid(row = 0 , column = 0, sticky = "news", padx = 20, pady = 10)

# Username label
username_frame = tkinter.Label(signup_frame, text = "Username")
username_frame.grid(row = 0 , column = 0)

# Password label
password_frame = tkinter.Label(signup_frame, text = "Password")
password_frame.grid(row = 2, column = 0)

# Username and password boxes
username_box = tkinter.Entry(signup_frame)
password_box = tkinter.Entry(signup_frame)
username_box.grid(row = 1, column = 0)
password_box.grid(row = 3, column = 0)

for widgets in signup_frame.winfo_children():
    widgets.grid_configure(padx = 10, pady = 5)

# Register button
register_button = tkinter.Button(frame1, text = "Register", command = entered_data)
register_button.grid(row = 1, column = 0, sticky = "nws", padx = 30, pady = 10)

# Username and password policy
policy_frame = tkinter.LabelFrame(frame1, text = "Username and password policies")
policy_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

username_policy = tkinter.Label(policy_frame, text = "Username must have at least 2 characters.")
password_policy = tkinter.Label(policy_frame, text = f"Password must have at least 8 characters which contain at least 1 number, 1 letter and 1 punctuation mark ({string.punctuation}).")
username_policy.grid(row = 0, column = 0, sticky = "nws")
password_policy.grid(row = 1, column = 0, sticky = "nws")

# Authenticate button
authenticate_button = tkinter.Button(frame1, text = "Authenticate", command = authentication)
authenticate_button.grid(row = 3, column = 0, sticky = "nws", padx = 30, pady = 10)

screen.mainloop()