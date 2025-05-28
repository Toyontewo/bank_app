import csv
import random
import os
import re
from getpass import getpass

CSV_FILE_PATH = "user_data.csv"


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def create_user_file_if_not_exists():
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Email", "Username", "Account Number", "Password", "Balance"])


def register_user():
    print("\n--- User Registration ---")
    f_name = input("Enter Your First Name: ")
    l_name = input("Enter Your Last Name: ")
    email = input("Enter Your Email: ")

    if not is_valid_email(email):
        print("Invalid email format. Try again.")
        return

    password = getpass("Enter your Password: ")
    password2 = getpass("Re-Enter your Password: ")

    if password != password2:
        print("Passwords do not match. Try again!")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    try:
        deposit_amt = float(input("Deposit amount ($): "))
        if deposit_amt <= 100:
            print("Amount must be greater than $100")
            return
    except ValueError:
        print("Invalid amount.")
        return

    username = f"{f_name}{l_name}".lower()
    account_number = random.randint(100000000, 999999999)

    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f_name, l_name, email, username, account_number, password, deposit_amt])

    print("Registration successful!\n")


def user_dashboard(user_row):
    while True:
        print("\n--- Account Dashboard ---")
        print("1. View Account Info\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            print(f"\nAccount Info:\nName: {user_row['First Name']} {user_row['Last Name']}\n"
                  f"Email: {user_row['Email']}\nUsername: {user_row['Username']}\n"
                  f"Account Number: {user_row['Account Number']}\nBalance: ${user_row['Balance']}")

        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                user_row['Balance'] = str(float(user_row['Balance']) + amount)
                update_user_balance(user_row['Username'], user_row['Balance'])
                print(f"Deposited ${amount}. New Balance: ${user_row['Balance']}")
            except ValueError:
                print("Invalid amount.")

        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: "))
                current_balance = float(user_row['Balance'])
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > current_balance:
                    print("Insufficient funds.")
                else:
                    user_row['Balance'] = str(current_balance - amount)
                    update_user_balance(user_row['Username'], user_row['Balance'])
                    print(f"Withdrew ${amount}. New Balance: ${user_row['Balance']}")
            except ValueError:
                print("Invalid amount.")

        elif choice == '4':
            try:
                receiver_acc = input("Enter receiver's account number: ")
                amount = float(input("Enter amount to transfer: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue

                sender_balance = float(user_row['Balance'])
                if amount > sender_balance:
                    print("Insufficient funds.")
                    continue

                rows = []
                receiver_found = False

                with open(CSV_FILE_PATH, mode='r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Account Number'] == receiver_acc:
                            receiver_found = True
                            print("\n--- Receiver Information ---")
                            print(f"Name: {row['First Name']} {row['Last Name']}\nEmail: {row['Email']}\nAccount Number: {row['Account Number']}")
                            confirm = input("\nConfirm transfer? (yes/no): ").strip().lower()
                            if confirm != 'yes':
                                print("Transfer cancelled.")
                                return
                            row['Balance'] = str(float(row['Balance']) + amount)
                        rows.append(row)

                if not receiver_found:
                    print("Receiver not found.")
                    continue
                
                user_row['Balance'] = str(sender_balance - amount)
                update_user_balance(user_row['Username'], user_row['Balance'])

                with open(CSV_FILE_PATH, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
                    writer.writeheader()
                    for row in rows:
                        if row['Username'] == user_row['Username']:
                            row['Balance'] = user_row['Balance']
                        writer.writerow(row)

                print(f"Successfully transferred ${amount} to account {receiver_acc}.")
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def update_user_balance(username, new_balance):
    rows = []
    with open(CSV_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username:
                row['Balance'] = new_balance
            rows.append(row)

    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def login_user():
    print("\n--- User Login ---")
    username_input = input("Enter Your Username: ")
    password_input = getpass("Enter Your Password: ")

    with open(CSV_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username_input and row['Password'] == password_input:
                print(f"Welcome back, {row['First Name']}!")
                user_dashboard(row)
                return

    print("Invalid username or password.\n")


def main():
    create_user_file_if_not_exists()
    while True:
        print("\nWelcome to Trust Bank Money App")
        print("1. Register\n2. Login\n3. Exit")
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            print("Thank you for using Trust Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
