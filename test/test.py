# Example usage:
username = input("Enter Username: ")
password = input("Enter Password: ")
if login_admin_staff(username, password):
    print("Login successful.")
else:
    print("Invalid username or password.")


def get_next_customer_id():
    try:
        with open("customer.txt", "r") as file:
            customers = file.readlines()
            if customers:
                last_customer_id = customers[-1].split(":")[1].strip()
                next_customer_id = int(last_customer_id) + 1
            else:
                next_customer_id = 1000
    except FileNotFoundError:
        next_customer_id = 1000
    return str(next_customer_id)


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