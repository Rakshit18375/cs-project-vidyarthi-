# Project Statement

**Project Title:** Personal Finance Manager (Command-Line Application)
**Student:** Rakshit Bisht
**Registration No.:** 26BCE10332
**Institution:** VIT
**Course Project:** VITyarthi – Build Your Own Project
**Language:** Python 3

---

## 1. Problem Statement

Many students and young earners have no simple way to record where their money comes from and where it goes. Spreadsheets feel heavy for quick entries, and full banking or budgeting apps are often complex, cloud-based, or tied to a bank account. Without a clear record of income and expenses, people lose track of their balance and find it hard to recall past transactions.

This project provides a lightweight, easy-to-use command-line tool that lets several users keep separate records of their income and expenses, check their balance at any time, and find past transactions quickly.

## 2. Objective

To design and build a menu-driven Personal Finance Manager in Python that:

- supports multiple users, each with a private list of transactions;
- records income and expense entries with an amount and a description;
- calculates the current balance automatically;
- lets a user search past transactions by keyword;
- handles invalid input without crashing.

## 3. Target Users

- Students managing pocket money, stipends, and daily expenses.
- Beginners who want a simple tool to track personal finances without any setup or internet connection.

## 4. Scope

### In scope

| Feature | Description |
|---|---|
| Add user | Create a new user profile with a unique username. |
| Login | Select an existing user and open their personal menu. |
| Add transaction | Record an *income* or *expense* with an amount (in ₹) and a description. |
| View all transactions | Display every transaction as a numbered list. |
| Check balance | Show the current balance (total income minus total expenses). |
| Search transactions | Find transactions whose description contains a keyword (case-insensitive). |
| Logout / Exit | Leave a user session or close the program. |

### Out of scope (current version)

- Permanent storage: data is kept in memory and is lost when the program exits.
- Passwords or authentication: login uses only a username.
- Editing or deleting transactions.
- Categories, budgets, charts, or reports.
- A graphical or web interface.

## 5. Functional Requirements

1. The system shall let a user be created only if the username is not already taken.
2. The system shall not accept empty text fields (username, description, keyword).
3. The system shall accept a transaction type only as `income` or `expense`.
4. The system shall accept only numeric amounts greater than zero and re-prompt on invalid input.
5. The system shall keep each user's transactions separate from other users.
6. The system shall compute the balance by adding income and subtracting expenses.
7. The system shall search descriptions without regard to upper or lower case and report when nothing matches.
8. The system shall show a friendly message for invalid menu choices instead of stopping.

## 6. Non-Functional Requirements

- **Usability:** Clear numbered menus and readable prompts.
- **Reliability:** Input validation loops prevent crashes from bad input.
- **Simplicity:** A single Python file with no external libraries required.
- **Portability:** Runs on any system with Python 3 installed.

## 7. Design Overview

The program is built around one class, `FinanceManager`.

- **Data structure:** A dictionary `users` maps each username to a list of transactions. Each transaction is a dictionary with the keys `type`, `amount`, and `description`.
- **Input helpers:** `gettext()` and `getamount()` validate user input.
- **User management:** `createuser()` and `login()`.
- **Transaction features:** `addtransaction()`, `transactions()`, `showbalance()`, and `search()`.
- **Menus:** `mainmenu()` handles adding users, logging in, and exiting; `menu()` is the per-user menu after login.

### Program Flow

```
Start
  └── Main Menu
        ├── 1. Add user  ──► create profile ──► back to Main Menu
        ├── 2. Login     ──► User Menu
        │                      ├── 1. Add transaction
        │                      ├── 2. View all transactions
        │                      ├── 3. Check balance
        │                      ├── 4. Search transactions
        │                      └── 5. Logout ──► back to Main Menu
        └── 3. Exit
```

## 8. Expected Outcome

A working console application that lets a user create a profile, record income and expenses, see an up-to-date balance, and search past entries, all with reliable input handling.

## 9. Future Enhancements

- Save data to a file or database so records persist between runs.
- Add password protection for user profiles.
- Support editing and deleting transactions.
- Add categories, monthly summaries, and budget alerts.
- Build a graphical or web interface.
