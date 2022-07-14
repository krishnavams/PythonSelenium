from abc import ABC, abstractmethod

# This class acts as design Specification
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        raise Exception

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)  # prints something in the console
    
class TextFileLogger(Logger):
    def __init__(self, file_object):
        self.file_object = file_object
    
    def log(self, message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()
        
class Spam(Logger):
    def demo(self):
        return "hello world"

# Composition (HAS-A relationship)
class FilteredLogger:
    def __init__(self, pattern, logger_type):
        self.pattern = pattern
        self.logger_type = logger_type
    # Polymorphic behavior or it is also called as Duck Typing
    def log(self, message):
        if self.pattern in message:
            self.logger_type.log(message)
            
# Function version
def filtered_logger(message, pattern, logger_type):
    if pattern in message:
        logger_type.log(message)

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        raise Exception
    
    @abstractmethod
    def withdraw(self, amount):
        raise Exception

    @abstractmethod
    def funds_transfer(self, amount):
        raise Exception
    
    @abstractmethod
    def statement(self):
        raise Exception

class SBI(BankAccount):
    # implement all funcs of BankAccount class
    pass

class HDFC(BankAccount):
    # implement all funcs of BankAccount class
    pass