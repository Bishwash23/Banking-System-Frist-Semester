def update_staff_details():
    print("\nUpdating staff details...\n")
    filename = STAFF
    
    # Authenticate admin staff
    while True:
        username_staff = input("Enter Admin Staff Username: ")
        password_staff = input("Enter Admin Staff Password: ")
        if login_admin_staff(username_staff, password_staff):
            print("Login successful.")
            break
        else:
            print("Invalid username or password.")
            print("Re-enter username and password.")
            continue
    
    # Prompt for staff username to update
    staff_username = input("Enter the username of the staff to update: ")
    
    # Check if the staff username exists
    if not username_available(filename, staff_username):
        # Initialize variables to store new details
        new_email = None
        new_password = None
        
        # Prompt for new email (if needed)
        while True:
            new_email = input("Enter new email (leave blank to keep current): ")
            if new_email == "":
                break
            elif not validate_email(new_email):
                print("Error: Invalid email format.")
                continue
            elif not email_available(filename, new_email) and new_email != staff_username:
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
        
        # Read existing staff details from file
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Open file in write mode to update staff details
        with open(filename, "w") as file:
            for line in lines:
                if line.strip().startswith("Username:"):
                    saved_username = line.split(":")[1].strip()
                    if saved_username == staff_username:
                        # Update email if provided
                        if new_email:
                            line = f"Email: {new_email}\n"
                        # Update password if provided
                        if new_password:
                            line = f"Password: {new_password}\n"
                file.write(line)
        
        # Print confirmation message
        print("\nStaff details updated successfully!")
        print_date_time() # function to print date and time
    else:
        print("Error: Staff username not found.")

