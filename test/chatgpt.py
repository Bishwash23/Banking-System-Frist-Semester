def login_customer(account_number, password):
    filename = CUSTOMER
    with open(filename, "r") as file:
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

        if account_number == saved_account_number and password == saved_password:
            return True

    return False

account_number = input("Enter your account number: ")
password = input("Enter your password: ")

if login_customer(account_number, password):
    print("Login successful!")
else:
    print("Invalid account number or password. Please try again.")
