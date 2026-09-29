class FinanceManager:

    def __init__(self):
        # Dictionary to store all users
        self.users = {}
    def transactions(self, username):
        print("\n--- All Transactions ---")
        transactions = self.users[username]
        if not transactions:
            print("No transactions yet.")
            return
        for i, t in enumerate(transactions, start=1):
            print(str(i) + ". [" + t["type"] + "] " + t["description"] 
                  + " - ₹" + str(t["amount"]))
    def getamount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                return amount
            except ValueError:
                print("That's not a valid amount. Try again.")
    def createuser(self):
        print("\n--- Create User ---")
        username = self.gettext("Enter username: ")
        if username in self.users:
            print("User already exists.")
            return
        self.users[username] = []
        print("User created successfully!")
    def gettext(self, prompt):
        while True:
            text = input(prompt).strip()
            if not text:
                print("This field can't be empty.")
                continue
            return text
    def login(self):
        print("\n--- Login ---")
        username = self.gettext("Enter username: ")
        if username not in self.users:
            print("User does not exist.")
            return
        print("\nWelcome, " + username + "!")
        self.menu(username)
    def addtransaction(self, username):
        print("\n--- Add Transaction ---")
        while True:
            kind = input("Type (income/expense): ").strip().lower()
            if kind in ("income", "expense"):
                break
            print("Please type either 'income' or 'expense'.")
        amount = self.getamount("Amount: ")
        description = self.gettext("Description: ")

        self.users[username].append({
            "type": kind,
            "amount": amount,
            "description": description
        })
        print("Transaction added!")
    def showbalance(self, username):
        balance = 0.0
        for t in self.users[username]:
            if t["type"] == "income":
                balance = balance + t["amount"]
            else:
                balance = balance - t["amount"]
        print("\nCurrent balance: ₹" + format(balance, ".2f"))
    def search(self, username):
        print("\n--- Search Transactions ---")
        transactions = self.users[username]
        if not transactions:
            print("Nothing to search yet.")
            return
        keyword = self.gettext("Enter a keyword: ").lower()
        found = False
        for i, t in enumerate(transactions, start=1):
            if keyword in t["description"].lower():
                print(
                    str(i) + ". [" + t["type"] + "] "
                    + t["description"] + " - ₹"
                    + format(t["amount"], ".2f")
                )
                found = True
        if not found:
            print("No matching transactions found.")
    def menu(self, username):
        while True:
            print("\n=== Personal Finance Manager ===")
            print("User: " + username)
            print("1. Add transaction")
            print("2. View all transactions")
            print("3. Check balance")
            print("4. Search transactions")
            print("5. Logout")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.addtransaction(username)
            elif choice == "2":
                self.transactions(username)
            elif choice == "3":
                self.showbalance(username)
            elif choice == "4":
                self.search(username)
            elif choice == "5":
                print("Logged out from " + username + ".")
                break
            else:
                print("That's not a valid choice.")
    def mainmenu(self):
        while True:
            print("\n===== PERSONAL FINANCE MANAGER =====")
            print("1. Add user")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.createuser()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("That's not a valid choice.")
def main():
    manager = FinanceManager()
    manager.mainmenu()
if __name__ == "__main__":
    main()
