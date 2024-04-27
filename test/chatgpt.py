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

# Example usage:
# account_number = 1234567890
# start_date = "2024-01-01"
# end_date = "2024-04-30"
# report = generate_statement_of_account_report(account_number, start_date, end_date)
# print(report)
