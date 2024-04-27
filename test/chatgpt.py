def deposit_money(account_number, deposited_amount, customer_filename, transaction_filename):
    # Read customer details from the customer file
    with open(customer_filename, 'r') as customer_file:
        customer_data = customer_file.read()
    
    # Find the customer with the given account number
    account_number_str = str(account_number)
    account_number_index = customer_data.find("Account Number: " + account_number_str)
    if account_number_index == -1:  # Account number not found
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
    new_balance = current_balance + deposited_amount
    
    # Update customer details in the customer file
    updated_customer_data = customer_data[:balance_index] + str(new_balance) + customer_data[balance_end_index:]
    with open(customer_filename, 'w') as customer_file:
        customer_file.write(updated_customer_data)
    
    # Write deposit details to the transaction file
    with open(transaction_filename, 'a') as transaction_file:
        transaction_file.write(f"Account Number: {account_number}\nTransaction Type: Deposit\nAmount: {deposited_amount}\nBalance: {new_balance}\n\n")

    print("Deposit successful.")
