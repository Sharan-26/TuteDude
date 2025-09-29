class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0
    
    def check_balance(self):
        print(f"Current balance: ${self._balance:.2f}")
        
    def deposit(self,amount):
        self._balance += amount
        print(f"Deposited: ${amount:.2f}")
        
    def withdraw(self,amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            
class SavingsAccount(Account):
    def __init__(self, id, holder_name, interest_rate):
        super().__init__(id, holder_name)
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        interest = self._balance * self.interest_rate / 100 # Calculate interest
        self._balance += interest # Apply interest to balance
        print(f"Applied interest: ${interest:.2f}")
        
class CurrentAccount(Account):
    def __init__(self,id,holder_name, overdraft_limit = 1000):
        super().__init__(id, holder_name)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit: # Check overdraft limit
            print("Overdraft limit exceeded!")
        else:
            self._balance -= amount # Allow overdraft
            print(f"Withdrew: ${amount:.2f}")  
            
class Bank:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.__accounts = {} # Private dictionary to store accounts
        
    def create_account(self,id,holder_name,type):
        if type == "savings":
            account = SavingsAccount(id,holder_name,interest_rate=5)
        elif type == "current":
            account = CurrentAccount(id,holder_name)
        self.__accounts[id] = account # Store account in dictionary
        print(f"Account created for {holder_name} with ID {id} as a {type} account.")
        return account
    
    def get_account(self,id):
        if id not in self.__accounts:
            print("Account not found!")
        else:
            account = self.__accounts[id] # Retrieve account from dictionary
            print(f"Account ID: {account.id}, Holder: {account.holder_name}")
            return account
    
bank = Bank("MyBank","New York")

bank.create_account(1,"Alice","savings")
bank.create_account(2,"Bob","current")

bank.get_account(1).deposit(500)
bank.get_account(1).apply_interest()
bank.get_account(1).check_balance()

#bank.get_account(2).deposit(300)
bank.get_account(2).withdraw(1001)
bank.get_account(2).check_balance()
