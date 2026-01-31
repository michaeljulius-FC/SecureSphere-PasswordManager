# =================================================================
# COPYRIGHT: (c) 2026 Collective-Fidelity. All Rights Reserved.
# PROJECT: SecureSphere Password Manager
# DESCRIPTION: A secure tool to generate and manage application passwords.
# =================================================================

import random
import string
import os

# --- STEP 1: INITIAL CONFIGURATION ---
# We define the files where our data will be stored.
# 'passwords.txt' holds the domain/password pairs.
# 'logs.txt' tracks every action taken by the user.
PASSWORD_FILE = "passwords.txt"
LOG_FILE = "logs.txt"

# For this collaborative effort, we define a simple master user database.
# In a real-world scenario, these would be hashed and stored securely.
users = {"admin": "SecureSphere2026"}

def log_action(user, action):
    """
    PURPOSE: This helper function records every event in the logs.txt file.
    WHAT HAPPENS: It opens the log file in 'append' mode so we don't delete old logs,
    then writes the username and the specific action they performed.
    """
    with open(LOG_FILE, "a") as f:
        f.write(f"USER: {user} | ACTION: {action}\n")

def generate_random_password(length=12):
    """
    PURPOSE: To create a high-security, 12-digit random password.
    WHAT HAPPENS: It combines uppercase letters, lowercase, digits, and symbols.
    It then uses the 'random' library to pick characters until the length is met.
    """
    # Define the pool of characters for maximum complexity
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the pool
    return ''.join(random.choice(characters) for i in range(length))

def add_password(user):
    """
    PURPOSE: To add a new password entry to our storage.
    WHAT HAPPENS:
    1. Asks for the domain (e.g., GitHub).
    2. Asks for a password. If the user leaves it blank, it calls our generator.
    3. Saves the domain and password into passwords.txt.
    """
    domain = input("Enter the domain name (e.g., GitHub): ")
    pwd = input("Enter password (leave blank to auto-generate a 12-digit secure password): ")
    
    if not pwd:
        pwd = generate_random_password()
        print(f"[*] Generated Secure Password: {pwd}")

    # Open the file in append mode to add the new entry
    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{domain} | {pwd}\n")
    
    print(f"[!] Successfully saved password for {domain}.")
    log_action(user, f"Added password for {domain}")

def retrieve_passwords(user):
    """
    PURPOSE: To display all stored passwords to the authorized user.
    WHAT HAPPENS: It checks if the file exists, reads every line, and prints it.
    """
    if not os.path.exists(PASSWORD_FILE):
        print("[!] No passwords have been stored yet.")
        return

    print("\n--- YOUR STORED PASSWORDS ---")
    with open(PASSWORD_FILE, "r") as f:
        for line in f:
            print(line.strip())
    log_action(user, "Retrieved all passwords")

def main():
    """
    PURPOSE: The central hub (Main Menu) of the application.
    WHAT HAPPENS: 
    1. It greets the user with the SecureSphere branding.
    2. It forces a login check.
    3. If successful, it enters a 'While' loop to keep the program running until the user exits.
    """
    print("="*60)
    print("  SECURESPHERE PASSWORD MANAGER - COLLECTIVE-FIDELITY  ")
    print("="*60)

    # Authentication Step
    username = input("Username: ")
    password = input("Master Password: ")

    if username in users and users[username] == password:
        print(f"\n[+] Welcome, {username}. Access Granted.")
        log_action(username, "Logged in successfully")
        
        while True:
            # Displaying the UI Menu
            print("\n" + "+" + "-"*38 + "+")
            print("| 1. Add New Password                 |")
            print("| 2. View All Passwords               |")
            print("| 9. Exit SecureSphere                |")
            print("+" + "-"*38 + "+")
            
            choice = input("Select an option: ")

            if choice == "1":
                add_password(username)
            elif choice == "2":
                retrieve_passwords(username)
            elif choice == "9":
                print("\n[!] Exiting. Your data remains protected. Stay safe!")
                log_action(username, "Logged out")
                break
            else:
                print("[X] Invalid choice. Please try again.")
    else:
        print("[X] Authentication Failed. Access Denied.")

if __name__ == "__main__":
    main()
