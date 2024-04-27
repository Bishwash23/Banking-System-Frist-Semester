
import os
from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# File to save the details
SUPER_USER = "super_user.txt"
ADMIN_STAFF = "admin_staff.txt"
STAFF = "staff.txt"
CUSTOMER = "customer.txt"
TRANSACTION_FILE = "transaction.txt"

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

# Function to delete staff account
def delete_staff_account():
    filename = STAFF
    print("\nDeleting staff account...\n")
    
    # Prompt for staff username to delete
    username = input("Enter the username of the staff to delete: ")

    # Check if staff username exists
    if not username_available(filename, username):
        # Read existing staff details from the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Open file in write mode to delete staff details
        with open(filename, 'w') as file:
            i = 0
            while i < len(lines):
                # Check if the line contains the details of the staff member with the given username
                if lines[i].strip().startswith("Username: ") and lines[i].split(":")[1].strip() == username:
                    # Skip the details of the staff member to delete
                    i += 5
                    continue
                # Write the line back to the file
                file.write(lines[i])
                i += 1
        
        print("Staff account deleted successfully.")
    else:
        print("Staff member not found. No account was deleted.")
    print_date_time()

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

# Function to delete customer account
def delete_customer_account(account_number):
    customer_filename = CUSTOMER
    transaction_filename = TRANSACTION_FILE

    # Remove customer details from the customer file
    with open(customer_filename, 'r') as customer_file:
        lines = customer_file.readlines()

    with open(customer_filename, 'w') as customer_file:
        deleted = False
        i = 0
        while i < len(lines):
            if lines[i].strip().startswith("Account Number: ") and lines[i].split(":")[1].strip() == str(account_number):
                # Remove the customer details
                del lines[i:i + 9]  # Assuming each customer record has 9 lines
                deleted = True
            else:
                customer_file.write(lines[i])
                i += 1

    if deleted:
        print("Customer account deleted successfully.")
    else:
        print("Customer account not found. No account was deleted.")

    # Remove transaction history associated with the account number
    with open(transaction_filename, 'r') as transaction_file:
        transactions = transaction_file.read()

    with open(transaction_filename, 'w') as transaction_file:
        # Split transactions by empty lines
        transaction_blocks = transactions.strip().split('\n\n')
        deleted_transactions = 0
        for block in transaction_blocks:
            if f"Account Number: {account_number}" not in block:
                # Write back transactions not associated with the account number
                transaction_file.write(block + '\n\n')
            else:
                deleted_transactions += 1

    if deleted_transactions > 0:
        print(f"Deleted {deleted_transactions} transactions associated with the account.")
    else:
        print("No transaction history found for the account.")

    print_date_time()  # Function to print date and time

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
    print_date_time()

# Function to read dob
def read_dob(account_number):
    filename = CUSTOMER
    
    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Initialize variable to store the date of birth
    dob = None
    
    # Iterate through each line in the file
    for i, line in enumerate(lines):
        # Check if the line contains the account number
        if line.strip().startswith("Account Number: ") and line.split(":")[1].strip() == str(account_number):
            # Retrieve the date of birth from the line two lines above
            dob = lines[i - 2].split(":")[1].strip()
            # Break the loop once the date of birth is found
            break
    
    return dob

# Function to deposit money to the customer account
def deposit_money(account_number, deposited_amount):
    customer_filename = CUSTOMER
    transaction_filename = TRANSACTION_FILE
    # Read customer details from the customer file
    with open(customer_filename, 'r') as customer_file:
        customer_data = customer_file.read()
    
    # Find the customer with the given account number
    account_number_str = str(account_number)
    account_number_index = customer_data.find("Account Number: " + account_number_str)
    if account_number_index == -1: # Account number not found
        print("Error: Account number not found.")
        return
    
    # Find the end index of the current customer's details
    end_index = customer_data.find("Account Number: ", account_number_index + len(account_number_str))
    if end_index == -1:  # If there is no next customer, set the end index to the end of the file
        end_index = len(customer_data)
    
    # Extract the customer's balance
    balance_index = customer_data.find("Balance: ", account_number_index, end_index) + len("Balance: ")
    balance_end_index = customer_data.find("\n", balance_index)
    current_balance = int(customer_data[balance_index:balance_end_index])
    
    # Calculate new balance after deposit
    new_balance = current_balance + int(deposited_amount)
    
    # Update customer details in the customer file
    updated_customer_data = customer_data[:balance_index] + str(new_balance) + customer_data[balance_end_index:]
    with open(customer_filename, 'w') as customer_file:
        customer_file.write(updated_customer_data)
    
    Date = current_time.strftime("%Y-%m-%d")
    Time = current_time.strftime("%H:%M:%S")
    # Write deposit details to the transaction file
    with open(transaction_filename, 'a') as transaction_file:
        transaction_file.write(f"Account Number: {account_number}\nTransaction Type: Deposit\nAmount: {deposited_amount}\nBalance: {new_balance}\nDate: {Date}\nTime: {Time}\n\n")

    print("Deposit successful.")

    print("New balance: ",new_balance)
    print_date_time()

# Function to withdraw money from customer account
def withdraw_money(account_number, withdrawn_amount):
    customer_filename = CUSTOMER
    transaction_filename = TRANSACTION_FILE
    
    # Read customer details from the customer file
    with open(customer_filename, 'r') as customer_file:
        customer_data = customer_file.read()
    
    # Find the customer with the given account number
    account_number_str = str(account_number)
    account_number_index = customer_data.find("Account Number: " + account_number_str)
    if account_number_index == -1: # Account number not found
        print("Error: Account number not found.")
        return
    
    # Find the end index of the current customer's details
    end_index = customer_data.find("Account Number: ", account_number_index + len(account_number_str))
    if end_index == -1:  # If there is no next customer, set the end index to the end of the file
        end_index = len(customer_data)
    
    # Extract the customer's account type
    account_type_index = customer_data.find("Account Type: ", account_number_index, end_index) + len("Account Type: ")
    account_type_end_index = customer_data.find("\n", account_type_index)
    account_type = customer_data[account_type_index:account_type_end_index].lower()
    
    # Extract the customer's balance
    balance_index = customer_data.find("Balance: ", account_number_index, end_index) + len("Balance: ")
    balance_end_index = customer_data.find("\n", balance_index)
    current_balance = int(customer_data[balance_index:balance_end_index])
    
    withdrawn_amount = int(withdrawn_amount)
    
    # Check if the withdrawal amount is valid
    if withdrawn_amount <= 0:
        print("Error: Invalid withdrawal amount.")
        return
    elif withdrawn_amount > current_balance:
        print("Error: Insufficient balance.")
        return
    
    # Check if the withdrawal amount violates the minimum balance requirement
    if account_type == "saving" and current_balance - withdrawn_amount < MIN_SAVING:
        print("Error: Minimum balance for saving accounts is RM", MIN_SAVING)
        return
    elif account_type == "current" and current_balance - withdrawn_amount < MIN_CURRENT:
        print("Error: Minimum balance for current accounts is RM", MIN_CURRENT)
        return
    
    # Calculate new balance after withdrawal
    new_balance = current_balance - withdrawn_amount
    
    # Update customer details in the customer file
    updated_customer_data = customer_data[:balance_index] + str(new_balance) + customer_data[balance_end_index:]
    with open(customer_filename, 'w') as customer_file:
        customer_file.write(updated_customer_data)
    
    Date = current_time.strftime("%Y-%m-%d")
    Time = current_time.strftime("%H:%M:%S")
    # Write withdrawal details to the transaction file
    with open(transaction_filename, 'a') as transaction_file:
        transaction_file.write(f"Account Number: {account_number}\nTransaction Type: Withdrawal\nAmount: {withdrawn_amount}\nBalance: {new_balance}\nDate: {Date}\nTime: {Time}\n\n")

    print("Withdrawal successful.")
    print("New balance: ", new_balance)
    print_date_time()

# Function to generate statement of account for customer
def generate_statement_of_account_report(account_number, start_date, end_date):
    transaction_filename = TRANSACTION_FILE
    
    # Initialize total deposits and total withdrawals
    total_deposits = 0
    total_withdrawals = 0
    
    # Read transactions from the transaction file
    with open(transaction_filename, 'r') as transaction_file:
        transactions = transaction_file.read().strip().split("\n\n")
    
    # Initialize statement of account report
    statement_report = f"Statement of Account Report for Account Number: {account_number}\n"
    statement_report += f"Period: {start_date} to {end_date}\n\n"
    
    # Iterate through transactions
    for transaction in transactions:
        lines = transaction.strip().split("\n")
        transaction_details = {}
        for line in lines:
            key, value = line.split(": ")
            transaction_details[key] = value
        
        # Check if the transaction is within the specified period and for the specified account number
        transaction_date = transaction_details["Date"]
        if start_date <= transaction_date <= end_date and int(transaction_details["Account Number"]) == account_number:
            transaction_type = transaction_details["Transaction Type"]
            amount = int(transaction_details["Amount"])
            
            # Update total deposits and withdrawals
            if transaction_type == "Deposit":
                total_deposits += amount
            elif transaction_type == "Withdrawal":
                total_withdrawals += amount
            
            # Add transaction details to the statement of account report
            statement_report += f"Date: {transaction_date}, Transaction Type: {transaction_type}, Amount: {amount}\n"
    
    # Add total deposits and withdrawals to the statement of account report
    statement_report += f"\nTotal Deposits: {total_deposits}\n"
    statement_report += f"Total Withdrawals: {total_withdrawals}\n"
    
    return statement_report

# Menu for login
while True:
    # Displaying main menu options
    print("\n\t\t===========================")
    print("\t\t===== WELCOME TO MBSS =====")
    print("\t\t===========================")
    print("\n1. Customer Login")
    print("2. Customer Register")
    print("3. Advanced")
    print("4. Exit")  # Option to exit the program
    
    # Getting user choice
    choice = input("\nEnter your choice: ")
    
    # Handling user choice
    if choice == "1":  # Customer login
        while True:
            # Displaying login options
            print("\n\t\t======================")
            print("\t\t===== LOGIN MENU =====")
            print("\t\t======================")
            print("\n1. Login")
            print("2. Exit")
            choice = input("\nEnter your choice: ")
            
            if choice == "1":  # User wants to login
                # Getting account number and password from user
                account_number = input("\nEnter your account number: ")
                password = input("Enter your password: ")
                
                # Checking if login credentials are valid
                if login_customer(account_number, password):
                    print("\nLogin successful!")
                    
                    # Checking if the password is the default one
                    stored_dob = read_dob(account_number)
                    default_password = default_password(stored_dob)
                    
                    if password == default_password:
                        # Prompting user to change default password
                        print("\nChange your default password")
                        new_password = input("\nEnter new password:")
                        
                        # Changing user's password
                        change_customer_password(account_number, default_password, new_password)
                        print("Your new password is:", new_password)
                        continue
                    while True:
                        # Displaying customer operation options
                        print("\n\t\t=========================")
                        print("\t\t===== CUSTOMER MENU =====")
                        print("\t\t=========================")
                        print("\n1. Deposit")
                        print("2. Withdrawal")
                        print("3. Change password")
                        print("4. Generate Statement")
                        print("5. Logout")
                        choice = input("\nEnter your choice: ")
                        
                        if choice == "1":  # Deposit money
                            print("\n\t\t========================")
                            print("\t\t===== DEPOSIT MENU =====")
                            print("\t\t========================")
                            deposited_amount = input("\nEnter amount to deposit: ")
                            deposit_money(account_number, deposited_amount)
                            continue
                        elif choice == "2":  # Withdraw money
                            print("\n\t\t=========================")
                            print("\t\t===== WITHDRAW MENU =====")
                            print("\t\t=========================")
                            withdrawn_amount = input("\nEnter amount to withdraw: ")
                            withdraw_money(account_number, withdrawn_amount)
                            continue
                        elif choice == "3":  # Change password
                            print("\nChange password...")
                            new_password = input("\nEnter new password: ")
                            change_customer_password(account_number, password, new_password)
                            print("\nPassword changed successfully.")
                            print("Your new password is:", new_password)
                            continue
                        elif choice == "4":  # Generate statement
                            print("\n\t\t=====================")
                            print("\t\t===== STATEMENT =====")
                            print("\t\t=====================")
                            start_date = input("\nEnter start date (YYYY-MM-DD): ")
                            end_date = input("Enter end date (YYYY-MM-DD): ")
                            report = generate_statement_of_account_report(account_number, start_date, end_date)
                            print(report)
                            continue
                        elif choice == "5":  # Logout
                            print("\nLogging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            continue
                else:
                    print("Invalid account number or password. Please try again.")
                    continue
            elif choice == '2':  # User wants to exit login
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
                continue
    elif choice == '2': # Customer Register
        register_customer()
        continue
    elif choice == '3':  # Advanced features
        while True:
            # Displaying advanced options
            print("\n\t\t========================")
            print("\t\t===== ADVANCE MENU =====")
            print("\t\t========================")
            print("\n1. Super Admin Login")
            print("2. Admin Staff Login")
            print("3. Exit")
            choice = input("\nEnter your choice: ")
            
            if choice == '1':  # Super admin login
                print("\n\t\t===================================")
                print("\t\t===== SUPER ADMIN LOGIN MENU =====")
                print("\t\t===================================")
                username = input("\nEnter Super Admin Username: ")
                password = input("Enter Super Admin Password: ")
                if login_super_user(username, password):
                    print("\nSuper Admin Login...")

                    while True:
                        print("\n\t\t============================")
                        print("\t\t===== SUPER ADMIN MENU =====")
                        print("\t\t============================")
                        print("\n1. Create a new Admin account")
                        print("2. Exit")
                        choice = input("\nEnter your choice: ")
                        
                        if choice == '1':  # Create a new admin account
                            create_admin_staff()
                            continue
                        elif choice == '2':  # Exit
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            continue
            elif choice == '2':  # Admin staff login
                print("\n\t\t============================")
                print("\t\t===== ADMIN LOGIN MENU =====")
                print("\t\t============================")
                username = input("\nEnter Admin Staff Username: ")
                password = input("Enter Admin Staff Password: ")
                if login_admin_staff(username, password):
                    while True:
                        print("\n\t\t======================")
                        print("\t\t===== ADMIN MENU =====")
                        print("\t\t======================")
                        print("\n1. Create a new Staff account")
                        print("2. Edit Staff account")
                        print("3. Edit customer account")
                        print("4. Delete staff account")
                        print("5. Delete customer account")
                        print("6. Exit")
                        choice = input("\nEnter your choice: ")
                        
                        if choice == '1':  # Create a new staff account
                            create_staff_account()
                            continue
                        elif choice == '2': # Edit Staff account
                            update_staff_details()
                            continue
                        elif choice == '3':  # Edit customer account
                            update_customer_details()
                            continue
                        elif choice == '4':  # Delete staff account
                            delete_staff_account()
                            continue
                        elif choice == '5':  # Delete customer account
                            print("\n Deleting customer account...")
                            account_number = input("Enter the account number of the customer you want to delete: ")
                            delete_customer_account(account_number)
                            continue
                        elif choice == '6':  # Exit
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            continue
    elif choice == '4':  # Exit the program
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

