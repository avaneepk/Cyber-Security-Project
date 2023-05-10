import psycopg2

conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="forum_server",
    user="postgres",
    password="avaneep")
c = conn.cursor()

#for registering account
def registration():
    while True:
        user_py= str(input("Username:"))
        passcode_py= str(input("Password:"))

        #funtion for checking password
        def validate_password(password):
            if len(password) < 8:
                return False

            has_uppercase = False
            has_digit = False
            has_special = False
        
            for char in password:
                if char.isupper():
                    has_uppercase = True
                elif char.isdigit():
                    has_digit = True
                elif not char.isalnum():
                    has_special = True

            return has_uppercase and has_digit and has_special
    
        #checking whether password is correct
        while not validate_password(passcode_py):
            print("Invalid password! Your password must meet the following criteria:")
            print("- At least 8 characters long")
            print("- Contains at least one capital letter")
            print("- Contains at least one number")
            print("- Contains at least one special character")
            passcode_py= str(input("Password:"))



        #function to insert registered data
        def register(user,passcode_2):
            c = conn.cursor()
            c.execute("INSERT INTO authenticate(username,passcode) VALUES (%s,%s)",(user,passcode_2))
            print("Registration Successful.")
            conn.commit()

        #checking whether the input username already exists
        def check_username(user_demo):
            c.execute("SELECT username FROM authenticate")
            records = c.fetchall()
            conn.commit()
            x=0
            for i in records:
                if i[0]==user_demo:
                    x=x+1
            if x>0:
                print("Username already in use. please try a different Username.\n")
            else:
                register(user_demo,passcode_py)




        check_username(user_py)

        #short menu for registration again
        menu_2=str(input("Another try? (write y/n):"))
        if menu_2=="n" or menu_2=="N":
            print("Registration closed.")
            break
        elif menu_2=="y" or menu_2=="Y":
            continue
        else:
            print("Wrong input. server has closed now.")
            break







#for logging in
def login():
    user_py= str(input("Username:"))
    passcode_py= str(input("Password:"))

    def authentication(username, password):
        # Check if the username and password match the records in the 'authenticate' table
        c.execute("SELECT username FROM authenticate WHERE username=%s AND passcode=%s",(username, password))
        result = c.fetchone()
        if result:
            print("You are authenticated, Welcome", username)
        else:
            print("Please enter correct username and password")

    authentication(user_py, passcode_py)


while True:
    option=int(input("Enter 1 if you want to register, 2 if you want to login, and 3 if you want to exit:"))
    if option == 1:
        registration()
    elif option == 2:
        login()
        break
    elif option == 3:
        print("The server is closed now.")
        break
    else:
        print("Please write only 1 or two")