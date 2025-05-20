


# Trust Bank Money App

A simple command-line banking application written in Python. This app simulates a basic banking system allowing users to register, log in, manage their account, and transfer funds—all data is persisted in a CSV file.

## Features

- ✅ Register with first name, last name, email, and password
- ✅ Auto-generate unique usernames and 9-digit account numbers
- ✅ Secure login using CSV-stored credentials
- ✅ Deposit and withdraw money
- ✅ Transfer funds to another user using account number
- ✅ View current account information
- ✅ CSV file automatically initialized if not present

## File Structure



.
├── app.py           # Main banking application logic
├── user\_data.csv    # Stores all user records (auto-created)
└── README.md        # Project documentation

````

```bash
git clone https://github.com/yourusername/trust-bank-app.git
cd trust-bank-app
````

2. **Run the application**

```bash
python app.py
```

3. **Choose an action from the menu**

```
Welcome to Trust Bank Money App
1. Register
2. Login
3. Exit
Select an option:
```

## 🧾 Sample Registration Fields

```
First Name: Toyo
Last Name: Ntewo
Email: toyontewo@python.com
Password: ********
Deposit amount ($): 200
```

## Notes

* Passwords are stored in **plain text** (for simplicity).
* This app is **not**, i repeat **NOT** intended for production use.

## Future Enhancements

* Add password encryption (e.g., `bcrypt`)
* Store and display transaction history
* Implement role-based access (e.g., admin controls)
* Create a GUI using Tkinter or Flask for a web-based version

