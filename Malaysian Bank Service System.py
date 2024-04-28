
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

# Function to create a default Super User Account
def create_super_user():
    # Default super user credentials
    super_user_data = {
        "username": "admin",
        "password": "admin@123"
    }
    # Check if the super user file does not exist
    if not os.path.exists(SUPER_USER):
        # If file does not exist, create it and write default super user details
        with open(SUPER_USER, 'w') as file:
            file.write(f"Username: {super_user_data['username']} \nPassword: {super_user_data['password']}")
    else:
        # If the file exists, do nothing
        return
create_super_user() # Call function to create the super user

# Function for authenticating a super user
def login_super_user(username, password):
    saved_username = None
    saved_password = None
    
    # Open the super user file for reading
    with open(SUPER_USER, "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line contains the username
            if line.strip().startswith("Username:"):
                # Extract the saved username
                saved_username = line.split(":")[1].strip()
            # Check if the line contains the password
            elif line.strip().startswith("Password:"):
                # Extract the saved password
                saved_password = line.split(":")[1].strip()
        
        # Check if the provided username and password match the saved credentials
        if username == saved_username and password == saved_password:
            # If they match, return True indicating successful authentication
            return True
        else:
            # If they do not match, return False indicating authentication failure
            return False
