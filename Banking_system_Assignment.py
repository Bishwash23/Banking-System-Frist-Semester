# Group members 1 tasks

import os
from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# File to save the details
SUPER_USER = "super_user.txt"
ADMIN_STAFF = "admin_staff.txt"
STAFF = "staff.txt"
CUSTOMER = "customer.txt"

# Function to create a default Super User Account
def create_super_user():
    super_user_data = {
        "username": "admin",
        "password": "admin@123"
    }
    if not os.path.exists(SUPER_USER):
        # If file does not exist, create it and write default super user details
        with open(SUPER_USER, 'w') as file:
            file.write(f"Username: {super_user_data['username']} \nPassword: {super_user_data['password']}")
    else:
        return

create_super_user() # Call function to create the super user

# Function for authenticating a super user
def login_super_user(username, password):
    saved_username = None
    saved_password = None
    
    with open(SUPER_USER, "r") as file:
        for line in file:
            if line.strip().startswith("Username:"):
                saved_username = line.split(":")[1].strip()
            elif line.strip().startswith("Password:"):
                saved_password = line.split(":")[1].strip()

        if username == saved_username and password == saved_password:
            return True
        else:
            return False

# Check username already exists or not
def username_available(filename, username):
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith("Username: "):
                existing_username = line.split(": ")[1].strip()
                if existing_username == username:
                    return False  # Username already exists
    return True  # Username is available

# Check email already exists or not
def email_available(filename, email):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith("Email: "):
                existing_email = line.split(": ")[1].strip()
                if existing_email == email:
                    return False  # Email already exists
    return True  # Email is available

# Basic email format validation
def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

# Function to create an admin staff account
def create_admin_staff():
    print("\nCreating admin staff account...\n")
    filename = ADMIN_STAFF
    name = input("Enter Name: ")
    
    # Validate and get a unique username
    while True:
        username = input("Enter Username: ")
        if not username_available(filename, username):
            print("Error: Username already exists.")
            continue
        else:
            break
    
    # Validate and get a unique email
    while True:
        email = input("Enter Email: ")
        if not email_available(filename, email):
            print("Error: Email already exists.")
            continue
        elif not validate_email(email):
            print("Error: Invalid email format.")
            continue
        else:
            break
    
    password = input("Enter Password: ")
    admin_staff_data = {
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }

    # Write admin staff details to file
    with open(filename, 'a') as file:
        file.write(f"Name: {admin_staff_data['name']}\nUsername: {admin_staff_data['username']}\nEmail: {admin_staff_data['email']}\nPassword: {admin_staff_data['password']}\n\n")
    
    # Print confirmation message
    print("\nAdmin Staff Account created successfully.")
    print("Name:", admin_staff_data['name'])
    print("Username:", admin_staff_data['username'])
    print("Email:", admin_staff_data['email'])
    print("Password:", admin_staff_data['password'])
    # Print date and time
    print("\nDate:", current_time.strftime("%Y-%m-%d"))
    print("Time:", current_time.strftime("%I:%M:%S %p"))

# Function to authenticate admin staff account
def login_admin_staff(username, password):
    filename = ADMIN_STAFF
    with open(filename, "r") as file:
        credentials = file.read().split("\n\n")

    # Iterate over each set of credentials
    for credential in credentials:
        lines = credential.split("\n")
        saved_username = None
        saved_password = None
        for line in lines:
            if line.strip().startswith("Username:"):
                saved_username = line.split(":")[1].strip()
            elif line.strip().startswith("Password:"):
                saved_password = line.split(":")[1].strip()

        if username == saved_username and password == saved_password:
            return True

    return False

# Function to create staff account
def create_staff_account():
    print("\nCreating staff account...\n")
    filename = STAFF
    name = input("Enter Name: ")
    
    # Validate and get a unique username
    while True:
        username = input("Enter Username: ")
        if not username_available(filename, username):
            print("Error: Username already exists.")
            continue
        else:
            break
    
    # Validate and get a unique email
    while True:
        email = input("Enter Email: ")
        if not email_available(filename, email):
            print("Error: Email already exists.")
            continue
        elif not validate_email(email):
            print("Error: Invalid email format.")
            continue
        else:
            break
    
    password = input("Enter Password: ")
    staff_data = {
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }

    # Write staff details to file
    with open(filename, 'a') as file:
        file.write(f"Name: {staff_data['name']}\nUsername: {staff_data['username']}\nEmail: {staff_data['email']}\nPassword: {staff_data['password']}\n\n")
    
    # Print confirmation message
    print("\nStaff Account created successfully.")
    print("Name:", staff_data['name'])
    print("Username:", staff_data['username'])
    print("Email:", staff_data['email'])
    print("Password:", staff_data['password'])
    # Print date and time
    print("\nDate:", current_time.strftime("%Y-%m-%d"))
    print("Time:", current_time.strftime("%I:%M:%S %p"))

create_staff_account()
# Function to authenticate staff account
def login_staff(username, password):
    filename = STAFF
    with open(filename, "r") as file:
        credentials = file.read().strip().split("\n\n")

    # Iterate over each set of credentials
    for credential in credentials:
        lines = credential.strip().split("\n")
        saved_username = None
        saved_password = None
        for line in lines:
            if line.strip().startswith("Username:"):
                saved_username = line.split(":")[1].strip()
            elif line.strip().startswith("Password:"):
                saved_password = line.split(":")[1].strip()

        if username == saved_username and password == saved_password:
            return True

    return False

