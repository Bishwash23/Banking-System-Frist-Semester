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
