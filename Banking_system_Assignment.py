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

# Minimum balance for customer accounts in RM
MIN_SAVING = 100
MIN_CURRENT = 500

# Function to print date and time
def print_date_time():
    print("\nDate:", current_time.strftime("%Y-%m-%d"))
    print("Time:", current_time.strftime("%I:%M:%S %p"))

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
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
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
    print_date_time() # function to print date and time

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
    print_date_time() # function to print date and time


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

# Function to calculate age
def calculate_age(dob):
    today = datetime.today()
    dob = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Function to generate unique Customer ID
def generate_unique_customer_id(filename):
    # Initialize counter
    customer_counter = 1
    
    # Read existing customer IDs from the file and update the counter if necessary
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.strip().startswith("Customer ID:"):
                    # Extract existing customer ID and update counter
                    existing_customer_id = line.split(":")[1].strip()
                    existing_customer_counter = int(existing_customer_id)
                    customer_counter = max(customer_counter, existing_customer_counter + 1)

    # Generate a new unique customer ID
    unique_customer_id = customer_counter
    
    # Increment the counter for the next customer
    customer_counter += 1

    return unique_customer_id

# Function to generate unique Account Number
def generate_unique_account_number(filename):
    # Initialize counter
    account_counter = 1
    
    # Read existing account numbers from the file and update the counter if necessary
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.strip().startswith("Account Number:"):
                    # Extract existing account number and update counter
                    existing_account_number = line.split(":")[1].strip()
                    existing_account_counter = int(existing_account_number)
                    account_counter = max(account_counter, existing_account_counter + 1)

    # Generate a new unique account number
    unique_account_number = account_counter
    
    # Increment the counter for the next account
    account_counter += 1

    return unique_account_number

# Function to generate a default password
def default_password(date_of_birth):
    password = "abc@" + date_of_birth
    return password
    
# Function to save customer details with unique identifiers (Customer ID and Account Number) after staff authentication
def save_customer_details(filename, name, email, date_of_birth, account_type, balance):
    print("\nLogin into Staff Account to save customer details.\n")
    
    # Generate unique Customer ID and Account Number
    customer_id = generate_unique_customer_id(filename)
    account_number = generate_unique_account_number(filename)
    
    password = default_password(date_of_birth)
    
    # Write customer details to file
    with open(filename, 'a') as file:
        file.write(f"Customer ID: {customer_id}\nName: {name}\nEmail: {email}\nDate of Birth: {date_of_birth}\nAccount Type: {account_type}\nAccount Number: {account_number}\nPassword: {password}\nBalance: {balance}\n\n")
    
    # Print confirmation message
    print("\nCustomer details saved successfully!")
    print("Customer ID:", customer_id)
    print("Account Number:", account_number)
    print("Password:", password)
    print_date_time() # function to print date and time

# Function to register customers
def register_customer():
    print("\nRegistering customer...\n")
    filename = CUSTOMER
    name = input("Enter Name: ")
    
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
    
    date_of_birth = input("Enter Date of Birth in AD (YYYY-MM-DD): ")
    
    # Calculate age
    age = calculate_age(date_of_birth)
    
    # Check if age is below 18
    if age < 18:
        print("Age is below 18. Not eligible to create an account.")
        return
    
    while True:
        account_type = input("Enter Account Type (Saving/Current): ").lower()
    
        # Validate account type
        if account_type not in ["saving", "current"]:
            print("Error: Invalid account type. Please enter 'Saving' or 'Current'.")
            continue
        else:
            break
    
    # Initialize balance with a default value
    balance = 0
    
    # Set initial balance based on account type
    if account_type == "saving":
        balance = MIN_SAVING
        
    elif account_type == "current":
        balance = MIN_CURRENT
        
    
    # Print confirmation message
    print("\nCustomer registered successfully.")
    print("Name:", name)
    print("Email:", email)
    print("Date of Birth:", date_of_birth)
    print("Account Type:", account_type)
    print_date_time() # function to print date and time
    save_customer_details(filename, name, email, date_of_birth, account_type, balance)

# Function to update staff details
def update_staff_details():
    filename = STAFF
    print("\nUpdating staff details...\n")
    
    # Prompt for staff username to update
    username = input("Enter the username of the staff to update: ")

    # Check if staff username exists
    if not username_available(filename, username):
        
        # Prompt for new email (if needed)
        while True:
            new_email = input("Enter new email (leave blank to keep current): ")
            if new_email == "":
                break
            elif not validate_email(new_email):
                continue
            elif not email_available(filename, new_email):
                print("Error: Email already exists.")
                continue
            else:
                break
        
        # Prompt for new password (if needed)
        while True:
            new_password = input("Enter new password (leave blank to keep current): ")
            if new_password == "":
                break
            else:
                break
        
        updated = False # Flag to track if any details were updated
        
        # Read existing staff details from the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Open file in write mode to update staff details
        with open(filename, 'w') as file:
            i = 0
            while i < len(lines):
                # Check if the line contains the details of the staff member with the given username
                if lines[i].strip().startswith("Username: ") and lines[i].split(":")[1].strip() == username:
                    # Update the email and password
                    if new_email != "":
                        lines[i + 1] = f"Email: {new_email}\n"
                    if new_password != "":
                        lines[i + 2] = f"Password: {new_password}\n"
                    
                    updated = True  # Set the flag to True indicating that details were updated
                # Write the line back to the file
                file.write(lines[i])
                i += 1
        
        if updated:
            print("Staff details updated successfully.")
    else:
        print("Staff member not found. No details were updated.")
    print_date_time()

# Function to update Customer details
def update_customer_details():
    filename = CUSTOMER
    print("\nUpdating Customer Details...\n")
    
    customer_id = input("Enter Customer ID of the customer to update: ")
    
    # Prompt for new email (if needed)
    while True:
        new_email = input("Enter new email (leave blank to keep current): ")
        if new_email == "":
            break
        elif not validate_email(new_email):
            continue
        elif not email_available(filename, new_email):
            print("Error: Email already exists.")
            continue
        else:
            break
    
    # Prompt for new account type (if needed)
    while True:
        new_account_type = input("Enter new account type (leave blank to keep current): ").lower()
        if new_account_type == "":
            break
        elif new_account_type not in ["saving", "current"]:
            print("Error: Invalid account type. Please enter 'Saving' or 'Current'.")
            continue
        else:
            break
    
    # Prompt for new password (if needed)
    while True:
        new_password = input("Enter new password (leave blank to keep current): ")
        if new_password == "":
            break
        else:
            break
    
    # Prompt for new balance (if needed)
    while True:
        new_balance = input("Enter new balance (leave blank to keep current): ")
        if new_balance == "":
            break
        else:
            break
    
    updated = False # Flag to track if any details were updated
    
    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Open file in write mode to update customer details
    with open(filename, 'w') as file:
        i = 0
        while i < len(lines):
            # Check if the line contains the details of the customer with the given customer ID
            if lines[i].strip().startswith("Customer ID: ") and lines[i].split(":")[1].strip() == str(customer_id):
                
                # Find the line numbers of relevant details
                email_index = i + 2
                account_type_index = i + 4
                password_index = i + 6
                balance_index = i + 7
                
                # Update the email if provided
                if new_email != "":
                    lines[email_index] = f"Email: {new_email}\n"

                # Update the account type if provided
                if new_account_type != "":
                    lines[account_type_index] = f"Account Type: {new_account_type}\n"

                # Update the password if provided
                if new_password != "":
                    lines[password_index] = f"Password: {new_password}\n"

                # Update the balance if provided
                if new_balance != "":
                    lines[balance_index] = f"Balance: {new_balance}\n"

                updated = True  # Set the flag to True indicating that details were updated
            # Write the line back to the file
            file.write(lines[i])
            i += 1

    if updated:
        print("Customer details updated successfully.")
    else:
        print("Customer not found. No details were updated.")
    print_date_time()

# Function to authenticate customer account
def login_customer(account_number, password):
    filename = CUSTOMER
    with open(filename, 'r') as file:
        customers = file.read().strip().split("\n\n")
    
    # Iterate over each set of customer details
    for customer in customers:
        lines = customer.strip().split("\n")
        saved_account_number = None
        saved_password = None
        for line in lines:
            if line.strip().startswith("Account Number:"):
                saved_account_number = line.split(":")[1].strip()
            elif line.strip().startswith("Password:"):
                saved_password = line.split(":")[1].strip()
        if saved_account_number == account_number and saved_password == password:
            return True
    return False

# Function to change password for customer
def change_customer_password(account_number, old_password, new_password):
    filename = CUSTOMER
    
    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Flag to track if the password was successfully changed
    password_changed = False
    
    # Open file in write mode to update customer password
    with open(filename, 'w') as file:
        i = 0
        while i < len(lines):
            # Check if the line contains the details of the customer with the given account number
            if lines[i].strip().startswith("Account Number: ") and lines[i].split(":")[1].strip() == str(account_number):
                
                # Find the line number of the password
                password_index = i + 1
                
                # Extract the old password
                saved_password = lines[password_index].split(":")[1].strip()
                
                # If the old password matches, update it with the new password
                if saved_password == old_password:
                    lines[password_index] = f"Password: {new_password}\n"
                    password_changed = True
                else:
                    print("Error: Old password does not match.")
                    return
                
            # Write the line back to the file
            file.write(lines[i])
            i += 1

    if password_changed:
        print("Password changed successfully.")
    else:
        print("Customer not found. Password not changed.")

# Function to read the password
def read_password(account_number):
    filename = CUSTOMER
    
    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Initialize variable to store the password
    password = None
    
    # Flag to indicate if the account number is found
    account_number_found = False
    
    # Iterate through each line in the file
    for line in lines:
        # Check if the line contains the details of the customer with the given account number
        if line.strip().startswith("Account Number: ") and line.split(":")[1].strip() == str(account_number):
            # Set the flag to indicate that the account number is found
            account_number_found = True
        # If the account number is found, look for the line containing the password
        elif account_number_found and line.strip().startswith("Password: "):
            # Extract the password
            password = line.split(":")[1].strip()
            # Break the loop once the password is found
            break
    
    return password

