class Account:
    _interest = 0.04  # leading underscore indicates that balance attribute is "private"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance     

    def _spam(self):
        print("Account _spam")
    
    def demo(self):
        self._spam()
        return self._interest

class SBAccount(Account):
    _interest = 0.05        # override _interest
    def _spam(self):    # override _spam
        print("Account _spam")
# -----------------------------------------------------------------------------------------
class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def mul(self):
        return self._a * self._b
# -----------------------------------------------------------------------------------------
class Account:
    __interest = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance     # leading underscore indicates that balance attribute is "private"

    def __spam(self):
        print("Account __spam")
    
    def demo(self):
        self.__spam()
        return self.__interest

class SBAccount(Account):
    __interest = 0.05        # override __interest?? NO ...
    def _spam(self):    # override __spam?? NO ....
        print("Account __spam")

# NOTE: Both single underscore and double underscore attributes can be accessed outside the class in python.
# 1.Single underscore attributes can be overriden in child class
# 2.Double underscore attributes cannot be overriden in child class
# -----------------------------------------------------------------------------------------
class Spam:
    def __init__(self, text):
        self.text = text

    def _clean_up(self, text):
        return text.strip()

    def split_text(self):
        temp = self._clean_up(self.text)
        return temp.split()

    def get_len(self):
        temp = self._clean_up(self.text)
        return len(temp)
# -----------------------------------------------------------------------------------------