class BankAccount : ##abstract ##parent
    def __init__(self,account_number:str,initial_balance=50000):
        self.account_number=account_number
        self._balance=initial_balance ##encapsulation
        self.is_active=True
        self.is_blocked=False
        self.transactions=[]
    @staticmethod
    def validate_amount(func):
        def wrapper(self,amount):
            if amount <=0:
                print("invalid amount") 
            else:
                return func (self,amount)
        return wrapper
    @staticmethod
    def check_balance(func):
        def wrapper(self,amount):
            if amount > self._balance :
                print("the amount is more than balance") 
            else:
                return func (self,amount)
        return wrapper
    @validate_amount
    def deposit(self,amount):
        if self.is_active :
            if self.is_blocked == False :
                self._balance += amount
                self.transactions.append(f'+{amount}')
            else:
                print("your account is blocked!")
        else:
            print("your account is inactivated")
    @check_balance
    @validate_amount
    def withdraw (self,amount):
        if self.is_active :
            if self.is_blocked == False :
                self._balance -= amount
                self.transactions.append(f'-{amount}')
            else:
                print("your account is blocked!")
        else:
            print("your account is inactivated")
    def get_balance(self):
        return self._balance
    
    def close_account (self):
        self.is_active =False
        print("")

    def block_account (self):
        self.is_blocked =True
        
    def calculate_profit(self):
        return 0


class SavingAccount (BankAccount): ##inheritance
    def __init__(self, account_number,profit, initial_balance=50000):
        super().__init__(account_number, initial_balance)
        self.profit=profit
    def calculate_profit(self):
        if self.is_active== False and self.is_blocked ==False:
            self._balance += self._balance*self.profit
            return self._balance
        self.transactions.append(self._balance)
    def __repr__(self):
        return f"\nsaving account\naccount number: {self.account_number}\nprofit: {self.profit}"

class CheckingAccount (BankAccount): ##inheritance
    def __init__(self, account_number,profit, initial_balance=50000):
        super().__init__(account_number, initial_balance)
        self.profit=profit
    def calculate_profit(self):
        if self.is_active== False and self.is_blocked ==False:
            self._balance += self._balance*self.profit
            return self._balance
        self.transactions.append(self._balance)
    def deposit(self, amount):  ##polymorphism
        return super().deposit(amount)
    def withdraw(self, amount):  ##polymorphism
        return super().withdraw(amount)
    def __repr__(self):
        return f"\nchecking account\naccount number: {self.account_number}\nprofit: {self.profit}"

class PremiumAccount(BankAccount):
    def __init__(self, account_number, initial_balance=50000,cashback_per=0.01,profit=0.1):
        super().__init__(account_number, initial_balance)
        self.cashback_per=cashback_per
        self.profit=profit
    @BankAccount.validate_amount
    @BankAccount.check_balance
    def withdraw(self, amount):
        if self.is_active :
            if self.is_blocked == False :
                        self._balance -= amount
                        result=amount*self.cashback_per
                        self._balance +=result
                        self.transactions.append(f'-{amount}')
                        self.transactions.append(f'+{result}')
            else:
                print("your account is blocked!")
        else:
            print("your account is inactivated")
    def __repr__(self):
        return f"\npremium account\naccount number: {self.account_number}\nprofit: {self.profit}"


class User:
    def __init__(self,full_name,date_of_birth,code):
        self.full_name=full_name
        self.date_of_birth=date_of_birth
        self.code=code
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
    def showinfo (self):
        return f"Full name: {self.full_name}\nDate of Birth: {self.date_of_birth}\nnational code:{self.code}\nAccounts: {self.accounts}"

class ATM:
    def __init__(self,language,password):
        self.language=language
        self.password=password
        self.is_blocked=False
    def deposit (self,account,amount):
        if self.is_blocked :
            print("the account is blocked")
            return "the account is blocked"
        account.deposit(amount)
    def withdraw (self,account,amount):
        if self.is_blocked :
            print("the account is blocked")
            return "the account is blocked"
        account.withdraw(amount)
    def block_card (self):
        self.is_blocked= True










user=User("asghar ahmadi","2010/11/1","1234")
saving=SavingAccount("9876",0.18)
checking=CheckingAccount("9876",0.05)
premium=PremiumAccount("9876")
user.add_account(premium)
user.add_account(saving)
user.add_account(checking)
# print(saving)
print(user.showinfo())
atm=ATM("persian","1122")

# atm.deposit(checking,200)
# atm.withdraw(checking,100)
# print(checking.transactions)
# print(checking.get_balance())
atm.deposit(premium,500000)
atm.withdraw(premium,600000)
# atm.withdraw(premium,200000)
# print(premium.transactions)
print(premium.get_balance())
