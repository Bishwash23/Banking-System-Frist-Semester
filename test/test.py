# Menu for login
print("1. Customer Login")
print("2. Customer Register")
print("3. Advanced")
choice = input("\nEnter your choice: ")

if choice == "1":
    while True:
        print("\nCustomer login...")
        account_number = input("\nEnter your account number: ")
        password = input("Enter your password: ")
        
        if login_customer(account_number, password):
            print("\nLogin successful!")
            
            stored_dob = read_dob(account_number)
            default_password = default_password(stored_dob)
            
            if password == default_password:
                print("\nChange your default password")
                new_password = input("\nEnter new password:")
                
                change_customer_password(account_number, default_password, new_password)
                
                print("\nPassword changed successfully.")
                print("Your new password is:", new_password)
                continue
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Change password")
            print("4. Logout")
            choice = input("\nEnter your choice: ")
            
        else:
            print("Invalid account number or password. Please try again.")