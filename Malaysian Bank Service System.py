
import os 
from datetime import datetime

# File to save the details
SUPER_USER = "super_user.txt"
ADMIN_STAFF = "admin_staff.txt"
STAFF = "staff.txt"
CUSTOMER = "customer.txt"
TRANSACTION_FILE = "transaction.txt"

# Minimum balance for customer accounts in RM
MIN_SAVING = 100
MIN_CURRENT = 500

def print_date_time():
    # Function to print the current date and time
    current_time = datetime.now()
    print("\nDate:", current_time.strftime("%Y-%m-%d"))
    print("Time:", current_time.strftime("%I:%M:%S %p"))

def create_super_user():
    # Function to create a default super user account if it doesn't exist
    super_user_data = {
        "username": "admin",
        "password": "admin@123"
    }
    # Check if the super user file does not exist
    if not os.path.exists(SUPER_USER):
        try:
            # Try to create super user file and write default credentials
            with open(SUPER_USER, 'w') as file:
                file.write(f"Username: {super_user_data['username']} \nPassword: {super_user_data['password']}")
        except IOError:
            # Handle IO errors if file creation fails
            print("Error creating super user file.")
    else:
        # If the file exists, do nothing
        return
create_super_user() # Call function to create the super user if it doesn't exits

def login_super_user(username, password):
    # Function to authenticate the super user
    saved_username = None
    saved_password = None
    try:
        # Try to open the super user file for reading
        with open(SUPER_USER, "r") as file:
            for line in file:
                if line.strip().startswith("Username:"):
                    saved_username = line.split(":")[1].strip()
                elif line.strip().startswith("Password:"):
                    saved_password = line.split(":")[1].strip()

        if username == saved_username and password == saved_password:
            # If provided credentials match saved credentials, return True
            return True
        else:
            # If credentials do not math, return False
            return False
    except IOError:
        # Handle IO errors if file reading fails
        print("Error reading super user file.")
        return False

# Check if a username is available in a given file
def username_available(filename, username):
    # If the file doesn't exist, create it
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass  # Create an empty file if it doesn't exist
    
    # Open the file and check for existing usernames
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line contains a username
            if line.strip().startswith("Username: "):
                # Extract the existing username
                existing_username = line.split(": ")[1].strip()
                # If the existing username matches the given username, it's not available
                if existing_username == username:
                    return False  # Username already exists
    # If the username is not found, it's available
    return True  # Username is available

# Check email already exists or not
def email_available(filename, email):
    # If the file doesn't exits, create it
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass # Create an empty file if it doesn't exist
    
    # Open the file and check for existing email
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line contains a email
            if line.strip().startswith("Email: "):
                # Extract the existing email
                existing_email = line.split(": ")[1].strip()
                # If the exiting email matches the given email, it's not available
                if existing_email == email:
                    return False  # Email already exists
    # If the email is not found, it's available
    return True  # Email is available

# Basic email format validation
def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

# Function to create admin staff account
def create_admin_staff():
    print("\nCreating admin staff account...\n")
    filename = ADMIN_STAFF
    
    # Input name
    name = input("Enter Name: ")
    
    # Validate and get a unique username
    while True:
        username = input("Enter Username: ")
        if not username_available(filename, username):
            print("Error: Username already exists.")
            continue
        elif len(username) < 5:  # Example: Minimum length requirement
            print("Error: Username must be at least 5 characters.")
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
    
    # Input and validate password
    while True:
        password = input("Enter Password: ")
        if len(password) < 8:  # Example: Minimum password length requirement
            print("Error: Password must be at least 8 characters.")
            continue
        else:
            break
    
    # Store admin staff data
    admin_staff_data = {
        "username": username,
        "name": name,
        "email": email,
        "password": password
    }

    # Write admin staff details to file
    try:
        with open(filename, 'a') as file:
            file.write(f"Username: {admin_staff_data['username']}\nName: {admin_staff_data['name']}\nEmail: {admin_staff_data['email']}\nPassword: {admin_staff_data['password']}\n\n")
    except IOError:
        print("Error writing to file.")
        return
    
    # Print confirmation message
    print("\nAdmin Staff Account created successfully.")
    print("Username:", admin_staff_data['username'])
    print("Name:", admin_staff_data['name'])
    print("Email:", admin_staff_data['email'])
    print_date_time()  # function to print date and time

# Function to login in admin staff account
def login_admin_staff(username, password):
    filename = ADMIN_STAFF
    
    # Check if the provided credentials match any admin staff account
    try:
        with open(filename, 'r') as file:
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

            # If the username and password match, login successful
            if username == saved_username and password == saved_password:
                return True
        # If no matching account is found, login unsuccessful
        return False
    except IOError:
        print("Error reding admin staff file.")

# Function to delete admin account
def delete_admin_account(username):
    filename = ADMIN_STAFF
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Find the index of the admin account to be deleted
        indexes_to_delete = []
        for i, line in enumerate(lines):
            if line.strip().startswith("Username:") and line.strip().split(":")[1].strip() == username:
                # Found the username to delete
                indexes_to_delete.append(i)
                indexes_to_delete.append(i + 1)  # Also delete the following lines containing name, email, password
                indexes_to_delete.append(i + 2)
                indexes_to_delete.append(i + 3)

        if indexes_to_delete:
            # Remove the lines corresponding to the admin account
            updated_lines = [line for i, line in enumerate(lines) if i not in indexes_to_delete]

            # Write the updated content back to the file
            with open(filename, 'w') as file:
                file.writelines(updated_lines)
            
            print(f"Admin account with username '{username}' deleted successfully.")
        else:
            print(f"Admin account with username '{username}' not found.")
    except IOError:
        print("Error reading or writing admin staff file.")

# Function to create staff account
def create_staff():
    print("\nCreating staff account...\n")
    filename = STAFF
    
    # Input name
    name = input("Enter Name: ")
    
    # Validate and get a unique username
    while True:
        username = input("Enter Username: ")
        if not username_available(filename, username):
            print("Error: Username already exists.")
            continue
        elif len(username) < 5:  # Example: Minimum length requirement
            print("Error: Username must be at least 5 characters.")
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
    
    # Input and validate password
    while True:
        password = input("Enter Password: ")
        if len(password) < 8:  # Example: Minimum password length requirement
            print("Error: Password must be at least 8 characters.")
            continue
        else:
            break
    
    # Store staff data
    admin_staff_data = {
        "username": username,
        "name": name,
        "email": email,
        "password": password
    }

    # Write staff details to file
    try:
        with open(filename, 'a') as file:
            file.write(f"Username: {admin_staff_data['username']}\nName: {admin_staff_data['name']}\nEmail: {admin_staff_data['email']}\nPassword: {admin_staff_data['password']}\n\n")
    except IOError:
        print("Error writing to file.")
        return
    
    # Print confirmation message
    print("\nAdmin Staff Account created successfully.")
    print("Username:", admin_staff_data['username'])
    print("Name:", admin_staff_data['name'])
    print("Email:", admin_staff_data['email'])
    print_date_time()  # function to print date and time

# Function to login in staff account
def login_staff(username, password):
    filename = STAFF
    
    # Check if the provided credentials match any staff account
    try:
        with open(filename, 'r') as file:
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

            # If the username and password match, login successful
            if username == saved_username and password == saved_password:
                return True
        # If no matching account is found, login unsuccessful
        return False
    except IOError:
        print("Error reding staff file.")

# Function to delete staff account
def delete_staff_account(username):
    filename = STAFF
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Find the index of the staff account to be deleted
        indexes_to_delete = []
        for i, line in enumerate(lines):
            if line.strip().startswith("Username:") and line.strip().split(":")[1].strip() == username:
                # Found the username to delete
                indexes_to_delete.append(i)
                indexes_to_delete.append(i + 1)  # Also delete the following lines containing name, email, password
                indexes_to_delete.append(i + 2)
                indexes_to_delete.append(i + 3)

        if indexes_to_delete:
            # Remove the lines corresponding to the staff account
            updated_lines = [line for i, line in enumerate(lines) if i not in indexes_to_delete]

            # Write the updated content back to the file
            with open(filename, 'w') as file:
                file.writelines(updated_lines)
            
            print(f"Staff account with username '{username}' deleted successfully.")
        else:
            print(f"Staff account with username '{username}' not found.")
    except IOError:
        print("Error reading or writing staff file.")

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
            elif len(new_password) < 8: # Minimum password length requirement
                print("Error: Password must be at least 8 characters.")
                continue
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
                        lines[i + 2] = f"Email: {new_email}\n"
                    if new_password != "":
                        lines[i + 3] = f"Password: {new_password}\n"
                    
                    updated = True  # Set the flag to True indicating that details were updated
                # Write the line back to the file
                file.write(lines[i])
                i += 1
        
        if updated:
            print("Staff details updated successfully.")
        else:
            print("No details were updated.")
    else:
        print("Staff member not found. No details were updated.")
    print_date_time() # Function to print date and time

# Function to calculate age
def calculate_age(dob):
    try:
        # Convert input dob to datetime object
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        
        # Get today's date
        today = datetime.today()
        
        # Check if dob is in the future
        if dob_date > today:
            return "Invalid date of birth. Please provide a date in the past."
        
        # Calculate age
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        
        return age
    except ValueError:
        return "Invalid date format. Please provide date in format YYYY-MM-DD."
