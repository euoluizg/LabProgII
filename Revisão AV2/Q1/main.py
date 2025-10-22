def login (username, password):
    # Simulate a login function
    if username and password == "admin":
        return True
    else:
        return False

username = input("Enter username: ")
password = input("Enter password: ")
if login(username, password):
    print("Login successful! Welcome,", username)
else:
    print("Login failed!")