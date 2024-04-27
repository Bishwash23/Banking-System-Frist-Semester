
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

# Get the current date and time
current_time = datetime.now()

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