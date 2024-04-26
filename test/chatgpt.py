def update_customer_details(customer_id, filename):
    print("\nUpdating customer details...\n")

    # Read existing customer details from the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    updated = False  # Flag to track if any details were updated

    # Open file in write mode to update customer details
    with open(filename, 'w') as file:
        i = 0
        while i < len(lines):
            # Check if the line contains the details of the customer with the given Customer ID
            if lines[i].strip().startswith("Customer ID: ") and lines[i].split(":")[1].strip() == str(customer_id):
                # Update the email, account type, password, and balance
                new_email = input("Enter new email (leave blank to keep current): ")
                new_account_type = input("Enter new account type (leave blank to keep current): ").lower()
                new_password = input("Enter new password (leave blank to keep current): ")
                new_balance = input("Enter new balance (leave blank to keep current): ")

                # Find the line numbers of relevant details
                email_index = i + 1
                account_type_index = i + 2
                password_index = i + 3
                balance_index = i + 4

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
