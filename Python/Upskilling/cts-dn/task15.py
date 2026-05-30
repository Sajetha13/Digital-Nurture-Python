def passcheck(user, pwd):
    if user=="" or pwd=="":
        print("Username and password cannot be empty")
    elif user=="admin":
        if pwd =="pass123":
            print("Login successful")
        else:
            print("Incorrect password")
    else:
        print("User not found")

username = "admin"
password = "pass123"
passcheck(username, password)

passcheck("", "")    
passcheck("admin", "wrongpass")