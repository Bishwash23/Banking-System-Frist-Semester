
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
