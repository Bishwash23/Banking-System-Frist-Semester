# Group members 1 tasks

import os
import datetime

# File to save the details
SUPER_USER = "super_user.txt"
ADMIN_STAFF = "admin_staff.txt"
STAFF = "staff.txt"
CUSTOMER = "customer.txt"

# Default password
PASSWORD = "password@123"

# Function to create a default Super User Account
def create_super_user():
    super_user_data = {
        "username": "admin",
        "password": "admin@123" # Default password for super user account
    }
    with open(SUPER_USER, 'w') as file:
        file.write(f"Username: {super_user_data['username']} \nPassword: {super_user_data['password']}")

# Function for authenticating a super user
def authenticate_super_user():
    # Check if super user account exists or not
    # If not, create a new one
    if not os.path.exists(SUPER_USER):
        create_super_user()
    
    super_user_username = input("Enter Super User Username: ")
    super_user_password = input("Enter Super User Password: ")
    
    with open(SUPER_USER, 'r') as file:
        stored_username = file.readline().split(": ")[1].strip()
        stored_password = file.readline().split(": ")[1].strip()
    
    if super_user_username == stored_username and super_user_password == stored_password:
        return True
    else:
        print("Error: Username or Password is incorrect")
        return False

# Function to create an admin staff account
def create_admin_staff():
    
    
    admin_name = input("\nEnter Admin Staff Full Name: ")
    admin_username = input("Enter Admin Staff Username: ")
    
    # Check if the entered username already exists
    if os.path.exists(ADMIN_STAFF):
        with open(ADMIN_STAFF, 'r') as file:
            existing_usernames = [line.split(": ")[1].strip() for line in file.readlines() if "Username:" in line]
        if admin_username == existing_usernames:
            print("Error: Username already exists. Please choose a different username.")
            return
    
    admin_password = input("Enter Admin Staff Password: ")
    
    # Write admin staff credentials to a text file
    with open(ADMIN_STAFF, 'a') as file:
        file.write(f"Name: {admin_name}\nUsername: {admin_username}\nPassword: {admin_password}\n")
    
    print("\nAdmin Staff Account Created Successfully!")
    print("\n\t\tLogin out Super User Account...")
create_admin_staff()
'''# Function to authenticate an admin staff account
def authenticate_admin_staff():
    admin_username = input("Enter Admin Staff Username: ")
    admin_password = input("Enter Admin Staff Password: ")
    
    # Check if admin staff account exists and credentials are correct
    if os.path.exists(ADMIN_STAFF):
        with open(ADMIN_STAFF, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                stored_username = lines[i+1].split(": ")[1].strip()
                stored_password = lines[i+2].split(": ")[1].strip()
                if admin_username == stored_username and admin_password == stored_password:
                    return True
    
    print("\nError: Incorrect Admin Staff Username or Password")
    return False

# Function to create a staff account
def create_staff_account():
    print("\n\t\tLogin in Admin Staff Account...")
    # Authenticate the admin staff
    if not authenticate_admin_staff():
        return
    print("\n\t\tCreating a staff account...")
    staff_name = input("Enter Staff Name: ")
    staff_username = input("Enter Staff Username: ")
    
    # Check if the entered username already exists
    if os.path.exists(STAFF):
        with open(STAFF, 'r') as file:
            existing_usernames = [line.split(': ')[1].strip() for line in file.readlines() if "Username:" in line]
        if staff_username == existing_usernames:
            print("Error: Username already exists. Please choose a different username.")
    
    staff_password = input("Enter Staff Password: ")
    
    # Write staff credentials to a text file
    with open (STAFF, 'a') as file:
        file.write(f"Name: {staff_name}\nUsername: {staff_username}\nPassword: {staff_password}\n")
    
    print("\nStaff Account Created Successfully!")
    print("\n\t\tLogin out Admin Staff Account...")

# Function to authenticate staff account
def authenticate_staff():
    staff_username = input("Enter Staff Username: ")
    staff_password = input("Enter Staff Password: ")

    # Check if staff account exits and credentials are correct
    if os.path.exists(STAFF):
        with open(STAFF, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                stored_username = lines[i+1].split(": ")[1].strip()
                stored_password = lines[i+2].split(": ")[1].strip()
                if staff_username == stored_username and staff_password == stored_password:
                    return True
    
    print("\nError: Incorrect Staff Username or Password")

# Function to generate a unique account number
def generate_unique_account_number():
    account_numbers = set()
    
    # Check if the file exists and read existing account numbers if it exists
    if os.path.exists(CUSTOMER):
        with open(CUSTOMER, 'r') as file:
            for line in file:
                if "Account Number:" in line:
                    account_numbers.add(int(line.split(": ")[1].strip()))
    
    # Generate a new account number
    if account_numbers:
        new_account_number = max(account_numbers) + 1
    else:
        new_account_number = 19801785700000 # Starting account number
    return new_account_number

# Function to register a customer
def register_customer():
    print("\n\t\tRegistering customer...")
    customer_name = input("Enter Customer Name: ")
    customer_account_type = input("Enter Customer Account Type (Savings/Current): ").lower()
    customer_address = input("Enter Customer Address: ")
    
    print("\n\t\tCustomer Registered Successfully!")
    save_customer_details(customer_name, customer_account_type, customer_address)

# Function to save customer details
def save_customer_details(customer_name, customer_account_type, customer_address):
    # Authenticate the admin staff or staff
    print("\n\t\tTo save customer detail Login in Staff Account...")
    if not authenticate_staff():
        return
    
    # Generate a unique account number
    customer_account_number = generate_unique_account_number()
    
    password = PASSWORD
    # Write customer details to a text file
    with open(CUSTOMER, 'a') as file:
        file.write(f"Name: {customer_name}\nAccount Type: {customer_account_type}\nAccount Number: {customer_account_number}\nPassword: {password}\nAddress: {customer_address}\n")
    
    print("\nAccount Number:", customer_account_number)
    print("Password:", password)
    print("\nCustomer Details Saved Successfully!")
    print("\n\t\tLogin out Staff Account...")

# Function to update staff and customer details (excluding names)
def update_details():
    # Authenticate the admin staff
    if not authenticate_admin_staff():
        return
    
    print("Which details do you want to update?")
    print("1. Staff Details")
    print("2. Customer Details")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        update_staff_details()
    elif choice == "2":
        update_customer_details()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

# Function to update staff details
def update_staff_details():
    print("What do you want to update?")
    update = input("Username or Password\n").lower()
    if update == "username":
        staff_username = input("Enter Staff Username to update: ")
        new_staff_username = input("Enter new Staff Username: ")
        with open(STAFF, 'r') as file:
            lines = file.readlines()
        with open(STAFF, 'a') as file:
            for i in range(0, len(lines), 3):
                if lines[i+1].split(": ")[1].strip() == staff_username:
                    lines[i+1] = f"Username: {new_staff_username}\n"
                    
                    file.write(lines[i])
                    file.write(lines[i+1])
                    file.write(lines[i+2])
                    print("Staff Details Update Successfully!")
                    break
                else:
                    print("Customer details do not match, Try again")
    elif update == "password":
        staff_password = input("Enter Staff Password to update: ")
        new_staff_password = input("Enter new Staff Password: ")
        with open(STAFF, 'r') as file:
            lines = file.readlines()
    
        with open(STAFF, 'a') as file:
            for i in range(0, len(lines), 3):
                stored_password = lines[i+2].split(": ")[1].strip()
                if staff_password == stored_password:
                    lines[i+2] = f"Password: {new_staff_password}\n"
                    
                    file.write(lines[i])
                    file.write(lines[i+1])
                    file.write(lines[i+2])
                    file.write(lines[i+3])
                    print("Staff Details Update Successfully!")
                    break
                else:
                    print("Staff details do not match, Try again")
                
    else:
        print("Invalid choice. Please enter either 'username' or 'password'.")

# Function to update Customer Details
def update_customer_details():
    print("What do you want to update?")
    update = input("Account Type or address\n").lower()
    if update == "account type":
        customer_account_type = input("Enter Customer Account Type to update: ")
        new_customer_account_type = input("Enter new Customer Account Type: ")
        with open(CUSTOMER, 'r') as file:
            lines = file.readlines()
        with open(CUSTOMER, 'a') as file:
            for i in range(0, len(lines), 6):
                stored_customer_account_type = lines[i+2].split(": ")[1].strip()
                if customer_account_type == stored_customer_account_type:
                    lines[i+2] = f"Account Type: {new_customer_account_type}\n"
                    file.write(lines[i])
                    file.write(lines[i+1])
                    file.write(lines[i+2])
                    file.write(lines[i+3])
                    file.write(lines[i+4])
                    file.write(lines[i+5])
                    print("Customer Details Updated Successfully!")
                    break
                else:
                    print("Customer details do not match, Try again")
                
    elif update == "address":
        customer_address = input("Enter Customer Address to update: ")
        new_customer_address = input("Enter new Customer Address: ")
        with open(CUSTOMER, 'r') as file:
            lines = file.readlines()
        with open(CUSTOMER, 'a') as file:
            for i in range(0, len(lines), 6):
                stored_customer_address = lines[i+5].split(": ")[1].strip()
                if customer_address == stored_customer_address:
                    lines[i+5] = f"Address: {new_customer_address}\n"
                    file.write(lines[i])
                    file.write(lines[i+1])
                    file.write(lines[i+2])
                    file.write(lines[i+3])
                    file.write(lines[i+4])
                    file.write(lines[i+5])
                    print("Customer Details Updated Successfully!")
                    break
                else:
                    print("Customer details do not match, Try again")
                
    else:
        print("Invalid choice. Please enter either 'account type' or 'address'.")

update_details()'''