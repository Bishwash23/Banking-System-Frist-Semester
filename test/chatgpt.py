# Function to generate Customer ID in sequence
def generate_unique_customer_id(filename):
    try:
        with open(filename, "r") as file:
            customers = file.readlines()
            if customers:
                last_customer_id = customers[-1].split(":")[1].strip()
                next_customer_id = int(last_customer_id) + 1
            else:
                next_customer_id = 1000
    except (FileNotFoundError, IndexError):
        next_customer_id = 1000
    return str(next_customer_id)
