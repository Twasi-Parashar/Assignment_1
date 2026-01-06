# Simple Login System

# Stored credentials (for demo purposes)
USERNAME = "admin"
PASSWORD = "admin123"

def login():
    print("=== Student Registration Login ===")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful! Welcome to the system.")
        return True
    else:
        print("Invalid username or password.")
        return False

# Run login
login()
