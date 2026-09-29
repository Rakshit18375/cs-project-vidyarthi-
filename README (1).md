# Personal Finance Manager

A simple command-line application written in Python for tracking personal income and expenses. Multiple users can be created, and each user has their own separate list of transactions. All amounts are in Indian Rupees (₹).

**Author:** Rakshit Bisht (Reg. No. 26BCE10332), VIT
**Course:** VITyarthi – Build Your Own Project

---

## Features

- **Multiple users** – create separate accounts and log in to each one.
- **Add transactions** – record an income or an expense with an amount and a description.
- **View all transactions** – see a numbered list of everything recorded.
- **Check balance** – total income minus total expenses.
- **Search transactions** – find transactions by a keyword in the description (case-insensitive).
- **Input validation** – rejects empty text, non-numeric amounts, zero or negative amounts, and invalid menu choices, and asks again instead of crashing.

## Requirements

- Python 3.6 or higher
- No external libraries (uses only built-in Python)

## How to Run

1. Save the code as `finance_manager.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python finance_manager.py
```

(On some systems use `python3` instead of `python`.)

## How to Use

**Main menu**

```
===== PERSONAL FINANCE MANAGER =====
1. Add user
2. Login
3. Exit
```

1. Choose **1** to create a user by entering a unique username.
2. Choose **2** and enter the username to log in.

**User menu (after login)**

```
=== Personal Finance Manager ===
1. Add transaction
2. View all transactions
3. Check balance
4. Search transactions
5. Logout
```

| Option | What it does |
|--------|--------------|
| 1 | Asks for type (`income` / `expense`), amount, and description, then saves it |
| 2 | Lists all transactions as `[type] description - ₹amount` |
| 3 | Shows the current balance (income − expenses) |
| 4 | Asks for a keyword and prints transactions whose description contains it |
| 5 | Logs out and returns to the main menu |

### Sample Session

```
===== PERSONAL FINANCE MANAGER =====
1. Add user
2. Login
3. Exit
Choose an option: 1
Enter username: rakshit
User created successfully!

Choose an option: 2
Enter username: rakshit
Welcome, rakshit!

Choose an option: 1
Type (income/expense): income
Amount: 5000
Description: Pocket money
Transaction added!

Choose an option: 1
Type (income/expense): expense
Amount: 250
Description: Books

Choose an option: 3
Current balance: ₹4750.00
```

## Code Structure

The whole program lives in a single class, `FinanceManager`.

| Method | Purpose |
|--------|---------|
| `__init__` | Creates the `users` dictionary that stores all data |
| `mainmenu` | Top-level menu: add user, login, exit |
| `createuser` | Adds a new username with an empty transaction list |
| `login` | Checks the user exists and opens the user menu |
| `menu` | Per-user menu loop (add, view, balance, search, logout) |
| `addtransaction` | Validates and stores a new transaction |
| `transactions` | Prints all transactions for a user |
| `showbalance` | Calculates and prints the balance |
| `search` | Keyword search over transaction descriptions |
| `getamount` | Input helper: repeats until a positive number is entered |
| `gettext` | Input helper: repeats until non-empty text is entered |

**Data structure:** `users` is a dictionary mapping each username to a list of transactions. Each transaction is a dictionary:

```python
{"type": "income" or "expense", "amount": 500.0, "description": "Salary"}
```

## Limitations

- Data is stored **in memory only**, so all users and transactions are lost when the program exits.
- There are no passwords; login only checks that the username exists.
- Transactions cannot be edited or deleted.

## Possible Future Improvements

- Save and load data using a file (JSON or CSV) or a database.
- Add password protection for users.
- Edit and delete transactions.
- Add categories and monthly summaries or reports.
- Add unit tests.
