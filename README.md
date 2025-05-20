


# Trust Bank Money App
This is a simple command-line banking application written in Python. It simulates a basic banking system that allows users to register, log in, manage their accounts, and transfer funds. All data is obtained from a CSV file.

## Features

- ✅ Register with first name, last name, email, and password
- ✅ Auto-generate unique usernames and 9-digit account numbers
- ✅ Secure login using CSV-stored credentials
- ✅ Deposit and withdraw money
- ✅ Transfer funds to another user using the account number
- ✅ View current account information
- ✅ CSV file automatically initialized if not present


```bash
git clone https://github.com/toyontewo/bank_app.git
cd bank_app
````

2. **Run the application**

```bash
python3 app.py
```

3. **Choose an action from the menu**

```
Welcome to Trust Bank Money App
1. Register
2. Login
3. Exit
Select an option:
```

## Sample Registration Fields

```
First Name: Toyo
Last Name: Ntewo
Email: toyontewo@python.com
Password: ********
Deposit amount ($): 200
```

## FYI

* Passwords are stored in **plain text** (for simplicity).
* This app is **not**, i repeat **NOT** intended for production use.

## Future Enhancements

* Add password encryption (e.g., `bcrypt`)
* Store and display transaction history
* Implement role-based access (e.g., admin controls)
* Create a GUI using Tkinter or Flask for a web-based version

