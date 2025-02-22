import psycopg2
import tkinter
import string
from tkinter import messagebox

conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="forum_server",
    user="postgres",
    password="")
c = conn.cursor()

def register(user,passcode_2):
    c = conn.cursor()
    c.execute("INSERT INTO authenticate(username,passcode) VALUES (%s,%s)",(user,passcode_2))
    conn.commit()

def check_username(user_demo, passcode_demo):
    c.execute("SELECT username FROM authenticate")
    records = c.fetchall()
    conn.commit()
    x=0
    for i in records:
        if i[0]==user_demo:
            x=x+1
    if x>0:
        tkinter.messagebox.showwarning(title = "Username Error", message ="Username already in use. please try a different Username.\n")
    else:
        return True

def authentication():
    username1 = username_box.get()
    password1 = password_box.get()
    # Check if the username and password match the records in the 'authenticate' table
    c.execute("SELECT username FROM authenticate WHERE username=%s AND passcode=%s",(username1, password1))
    result = c.fetchone()
    if result:
        tkinter.messagebox.showinfo(title = "Successful Authentication", message = f"You are authenticated! Welcome {username1}")
    else:
        tkinter.messagebox.showwarning(title = "Failed Authentication", message = f"Please enter correct username and password")


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
            if check_username(username, password):
                tkinter.messagebox.showinfo(title = "Registration Status", message = "Registration Successful!")
                register(username, password)
        else:
            tkinter.messagebox.showwarning(title = "Incorrect Password", message =f"Password must have at least 8 characters which contain at least 1 number, 1 letter and 1 punctuation mark ({string.punctuation}).")
                
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
