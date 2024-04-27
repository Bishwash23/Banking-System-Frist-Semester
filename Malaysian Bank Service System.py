
import os 
from datetime import datetime

# File to save the details
SUPER_USER = "super_user.txt"
ADMIN_STAFF = "admin_staff.txt"
STAFF = "staff.txt"
CUSTOMER = "customer.txt"
TRANSACTION_FILE = "transaction.txt"

# Minimum balance for customer accounts in RM
MIN_SAVING = 100
MIN_CURRENT = 500

# Get the current date and time
current_time = datetime.now()