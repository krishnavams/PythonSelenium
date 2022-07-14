from datetime import datetime

# Custom Exceptions for Bank Transactions!!
class TransactionDeclined(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class MaxWithdrawLimtExceeded(Exception):
    pass


class BankAccount:
    interest_rate = 4.0
    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = float(amount)
        self._transactions = [ ]
        self._transactions.append(f"{datetime.now()} ***Initial Deposit*** {self.amount}")

    def deposit(self, amount):
        self.balance += float(amount)
        self._transactions.append(f'{datetime.now()} Deposited Amount: {amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._transactions.append(f'{datetime.now()} Withdrawn Amount: {amount}')
        else:
            raise InsufficientBalance()

    def statement(self):
        for line in self._transactions:
            print(line)
        print(f"Total Account Balance: {self.balance}")

    def roi(self):
        self.balance = self.balance + self.balance * (self.interest_rate / 100)


class SavingsAccount(BankAccount):
    interest_rate = 4.0
    def withdraw(self, amount):
        if amount > 10000:
            raise MaxWithdrawLimtExceeded('Can not withdrawn more than 10000 per day')
        super().withdraw(amount)


class SalaryAccount(BankAccount):
    MAX_DRAFT_AMOUNT = 10000
    def __init__(self, name):
        self.is_first_month_salary = True
        self.draft_amount = 0
        super().__init__(name, 0.00)    
    
    def deposit(self, amount):
        if self.is_first_month_salary:
            self.is_first_month_salary = False
            super().deposit(amount + 1000)
        else:
            super().deposit(amount)
    
    def overdraft(self, amount):
        if self.draft_amount + amount <= self.MAX_DRAFT_AMOUNT:
            self.draft_amount += amount
            super().deposit(amount)     # handover the amount to deposit method of parent class
        else:
            raise ValueError(f"Max available draft amount is {self.MAX_DRAFT_AMOUNT - self.draft_amount}")


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.5

    def withdraw(self, amount):
        if amount > 20000:
            raise MaxWithdrawLimtExceeded('Can not withdraw more than 20000 per day')
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 9.5

    def deposit(self, amount):
        if amount < 1000:
            raise ValueError('Min Amount Should be 1000rs')
        super().deposit(amount)

    # Completely overriding the parent class method "withdraw"
    def withdraw(self, amount):
        raise TransactionDeclined("Can not withdraw")


class PenaltyAccount:
    def withdraw(self, amount):
        self.balance -= 200  # Penalty for withdrawing from PensionAccount
        super().withdraw(amount)

class RetirementAccount(PenaltyAccount, BankAccount):
    pass

# ====================================================
# Alternate solution
class PenaltyAccount:
    penalty = 0
    def withdraw(self, amount):
        self.balance -= self.__class__.penalty  # Penalty for withdrawing from PensionAccount
        super().withdraw(amount)

class RetirementAccount(PenaltyAccount, BankAccount):
    penalty = 200       # Over-riding class variable

class MaxTransactionLmit(PenaltyAccount, BankAccount):
    penalty = 1000  # Over-riding class variable

# ====================================================
# Alternate solution
class PenaltyAccount:
    def __init__(self, penalty_amount):
        self.penalty_amount = penalty_amount

    def withdraw(self, amount):
        self.balance -= self.penalty_amount
        super().withdraw(amount)

class PensionAccount(PenaltyAccount, BankAccount):
    def __init__(self, penalty_amount, name, balance):
        PenaltyAccount.__init__(self, penalty_amount)       # Initialise the constructor of PenaltyAccount class
        BankAccount.__init__(self, name, balance)       # Initialise the constructor of BankAccount class
# ====================================================