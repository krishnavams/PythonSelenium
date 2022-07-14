# -------------------------------------------------------------------------------
# problem with sub-classes
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class CSVFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        import csv
        csv_writer = csv.writer(self.file)
        csv_writer.writerow(message)
        self.file.flush()

class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)
            
# -------------------------------------------------------------------------------
# Customized Logger class
class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.log(message)

# Implementation of each class is hidden from the user.
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class CSVFileLogger:
    def __init__(self, file):
        self.file = file
    
    def log(self, message):
        import csv
        csv_writer = csv.writer(self.file)
        row = message.split()
        csv_writer.writerow(row)
        self.file.flush()

class FilteredLogger:
    def __init__(self, *, pattern, handler):
        self.pattern = pattern
        self.handler = handler

    def log(self, message):
        if self.pattern in message:
            self.handler.log(message)

log1 = FilteredLogger(pattern="error", handler=ConsoleLogger())
log2 = FilteredLogger(pattern="info", handler=TextFileLogger(open("test.txt")))
# -------------------------------------------------------------------------------
class BankAccount:
    def __init__(self, account_type):
        self.account_type = account_type

    def deposit(self, amount):
        self.account_type.deposit(amount)
    
    def withdraw(self, amount):
        self.account_type.withdraw(amount)

class CustomerInfo:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = [ ]

class SBAccount(CustomerInfo):
    interest_rate = 0.04
    def deposit(self, amount):
        self.balance +=amount
    
    def withdraw(self, amount):
        self.balance -= amount

class SalaryAccount(CustomerInfo):
    MAX_LIMIT = 5000
    def __init__(self, name):
        self.od = 0
        super().__init__(name, 0)

    def deposit(self, amount):
        self.balance= 1000
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def over_draft(self, amount):
        if self.od + amount <= self.MAX_LIMIT:
            self.balance += amount
            self.od += amount
        else:
            raise ValueError("Max OD reached")

class PFAccount(CustomerInfo):
    interest_rate = 0.085
    def withdraw(self, amount):
        self.balance -= amount + 100

b1 = BankAccount(SBAccount("sandeep", 1000))
s2 = BankAccount(SalaryAccount("sandeep"))
pf = BankAccount(PFAccount("sandeep", 1000))