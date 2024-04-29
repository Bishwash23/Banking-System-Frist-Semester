
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

# Function to generate unique Customer ID
def generate_unique_customer_id():
    filename = CUSTOMER
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
def generate_unique_account_number():
    filename = CUSTOMER
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

# Function to save customer details
def save_customer_details(filename, name, email, date_of_birth, account_type, balance):
    print("\nLogin into Staff Account to save customer details.\n")
    while True:
        username = input("Enter Staff username: ")
        password = input("Enter Staff password: ")
        
        # Assuming login_staff function handles staff authentication
        if login_staff(username, password):
            # Generate unique Customer ID and Account Number
            customer_id = generate_unique_customer_id()
            account_number = generate_unique_account_number()
            
            password = default_password(date_of_birth)
            
            # Write customer details to file
            with open(filename, 'a') as file:
                # Write account number in the second column
                file.write(f"Customer ID: {customer_id}\nAccount Number: {account_number}\n")
                file.write(f"Name: {name}\nEmail: {email}\nDate of Birth: {date_of_birth}\nAccount Type: {account_type}\nPassword: {password}\nBalance: {balance}\n\n")
            
            # Print confirmation message
            print("\nCustomer details saved successfully!")
            print("Customer ID:", customer_id)
            print("Account Number:", account_number)
            print("Name: ", name,"\nDate of Birth: ", date_of_birth,"\nAccount Type: ", account_type)
            print("Password:", password)
            print_date_time() # Function to print date and time
            break
        else:
            print("Invalid staff credentials. Unable to save customer details. Try again.\n")
            continue

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
    
    # Prompt for Date of Birth
    while True:
        date_of_birth = input("Enter Date of Birth in AD (YYYY-MM-DD): ")
        age = calculate_age(date_of_birth)
        if isinstance(age, int):
            if age < 18:
                print("Age is below 18. Not eligible to create an account.")
                return
            else:
                break
        else:
            print(age) # Print the error message if date of birth is invalid
            continue
    
    # Prompt for Account Type
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

# Check if Customer ID or Account Number is in the file
def customer_id_check(customer_id):
    filename = CUSTOMER
    # If the file doesn't exist, create it
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass # Create an empty file if it doesn't exist
    
    # Open the file and check for existing usernames
    with open (filename, 'r') as file:
        for line in file:
            # Check if the line contains a username
            if line.strip().startswith("Customer ID: "):
                # Extract the existing customer ID
                existing_customer_id = line. split(": ")[1].strip()
                # If the existing customer ID matches the given customer ID
                if existing_customer_id == customer_id:
                    return True # Customer ID available
    # IF the customer ID is not found , it's unavailable
    return False

# Function to update Customer details
def update_customer_details():
    filename = CUSTOMER
    print("\nUpdating Customer Details...\n")
    
    customer_id = input("Enter Customer ID of the customer to update: ")
    if customer_id_check(customer_id):
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
            elif len(new_password) < 8: # Minimum password length requirement
                print("Error: Password must be at least 8 characters.")
                continue
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
                    email_index = i + 3
                    account_type_index = i + 5
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

# Function to delete customer account
def delete_customer_account(account_number):
    customer_file = CUSTOMER
    transaction_file = TRANSACTION_FILE
    
    # Initialize flag to check if customer account is found
    account_found = False
    
    # Read customer details from file
    try:
        with open(customer_file, 'r') as file:
            customer_lines = file.readlines()
    except IOError:
        print("Error reading customer file.")
        return
    
    # Find the index of the customer account to be deleted
    customer_indexes_to_delete = []
    for i in range(len(customer_lines)):
        if customer_lines[i].strip().startswith("Account Number:") and customer_lines[i].strip().split(":")[1].strip() == account_number:
            # Found the account number to delete
            account_found = True
            # Append the index of customer details to delete
            customer_indexes_to_delete.append(i - 2)
            customer_indexes_to_delete.append(i - 1)
            customer_indexes_to_delete.append(i)
            customer_indexes_to_delete.append(i + 1)  # Also delete the following lines containing customer details
            customer_indexes_to_delete.append(i + 2)
            customer_indexes_to_delete.append(i + 3)
            customer_indexes_to_delete.append(i + 4)
            customer_indexes_to_delete.append(i + 5)
            customer_indexes_to_delete.append(i + 6)
    
    if account_found:
        # Remove the lines corresponding to the customer account
        updated_customer_lines = [line for i, line in enumerate(customer_lines) if i not in customer_indexes_to_delete]
        
        # Write the updated customer details back to the file
        try:
            with open(customer_file, 'w') as file:
                file.writelines(updated_customer_lines)
        except IOError:
            print("Error writing customer file.")
            return
        
        print(f"Customer account with account number '{account_number}' deleted successfully.")
        
        # Delete transaction history associated with the account number
        try:
            with open(transaction_file, 'r') as file:
                transaction_lines = file.readlines()
        except IOError:
            print("Error reading transaction file.")
            return
        
        # Find the indexes of transaction history to delete
        transaction_indexes_to_delete = []
        for i in range(len(transaction_lines)):
            if transaction_lines[i].strip().startswith("Account Number:") and transaction_lines[i].strip().split(":")[1].strip() == account_number:
                # Found the account number in transaction history to delete
                transaction_indexes_to_delete.append(i - 1)
                transaction_indexes_to_delete.append(i)
                transaction_indexes_to_delete.append(i + 1)  # Also delete the following lines containing transaction details
                transaction_indexes_to_delete.append(i + 2)
                transaction_indexes_to_delete.append(i + 3)
                transaction_indexes_to_delete.append(i + 4)
                transaction_indexes_to_delete.append(i + 5)
        
        # Remove the lines corresponding to the transaction history
        updated_transaction_lines = [line for i, line in enumerate(transaction_lines) if i not in transaction_indexes_to_delete]
        
        # Write the updated transaction history back to the file
        try:
            with open(transaction_file, 'w') as file:
                file.writelines(updated_transaction_lines)
        except IOError:
            print("Error writing transaction file.")
            return
        
        print(f"Transaction history associated with account number '{account_number}' deleted successfully.")
        
    else:
        print(f"Customer account with account number '{account_number}' not found.")

# Function to login in customer account
def login_customer(account_number, password):
    filename = CUSTOMER
    
    try:
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Initialize variables to store customer details
            stored_account_number = None
            stored_password = None
            
            # Iterate over each line in the file
            for line in lines:
                # Check if the line contains Account Number or Password
                if line.strip().startswith("Account Number:"):
                    stored_account_number = line.split(":")[1].strip()
                elif line.strip().startswith("Password:"):
                    stored_password = line.split(":")[1].strip()
                
                # If both Account Number and Password are found, check for a match
                if stored_account_number and stored_password:
                    # Check if the provided Account Number and Password match
                    if account_number == stored_account_number and password == stored_password:
                        # Return True if login is successful
                        return True
    
    except IOError:
        print("Error reading customer file.")
    
    # Return False if Account Number or Password doesn't match or if there's an error reading the file
    return False

