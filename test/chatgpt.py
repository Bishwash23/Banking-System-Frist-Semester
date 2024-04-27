def get_customer_password(account_number):
    filename = CUSTOMER
    
    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Initialize variable to store the password
    password = None
    
    # Iterate through each line in the file
    for line in lines:
        # Check if the line contains the details of the customer with the given account number
        if line.strip().startswith("Account Number: ") and line.split(":")[1].strip() == str(account_number):
            # Extract the password
            password = line.split(":")[1].strip()
            break
    
    return password
