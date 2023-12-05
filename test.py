user_credentials = {}

def register(username, password):
    if username in user_credentials:
        print("Username already exists. Please try another one.")
    else:
        user_credentials[username] = password
        print(f"Welcome, {username}! You have successfully registered.")

def login(username, password):
    if username in user_credentials:
        if user_credentials[username] == password:
            print(f"Welcome back, {username}!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register.")

def update_password(username, old_password, new_password):
    if username in user_credentials:
        if user_credentials[username] == old_password:
            user_credentials[username] = new_password
            print("Password successfully updated.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register.")

while True:
    action = input("Enter 'register' to register, 'login' to login, or 'update' to update your password: ")
    if action == 'register':
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        register(username, password)
    elif action == 'login':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    elif action == 'update':
        username = input("Enter your username: ")
        old_password = input("Enter your current password: ")
        new_password = input("Enter your new password: ")
        update_password(username, old_password, new_password)
    else:
        print("Invalid action. Please try again.")