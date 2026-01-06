# User database (username : password)
users = {
    "admin": "admin123",
    "student1": "stud123",
    "student2": "stud456"
}

def login():
    print("=== Login System ===")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}.")
        return True
    else:
        print("Login failed. Invalid credentials.")
        return False

# Run the login function
login()
