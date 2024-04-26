print_date_time() # function to print date and time
    
# Example usage:
username = input("Enter Username: ")
password = input("Enter Password: ")
if login_admin_staff(username, password):
    print("Login successful.")
else:
    print("Invalid username or password.")
