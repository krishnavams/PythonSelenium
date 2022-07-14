import csv

# Logging classes
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message +"\n")
        self.file.flush()

class CSVLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        words = message.split()
        csv_writer = csv.writer(self.file)
        csv_writer.writerow(words)
        self.file.flush()

# Passing the "pattern" as constructor argument
class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)

class FilteredTextLogger(FilteredLogger, TextLogger):
    def __init__(self, pattern, file):
        FilteredLogger.__init__(self, pattern)
        TextLogger.__init__(self, file)

fcl = FilteredConsoleLogger("ERROR")
ftl = FilteredTextLogger("ERROR", open('test.txt', 'w'))
# ----------------------------------------------------------------------------------------------
# "pattern" as class variable
class FilteredLogger:
    pattern = None  # class variable
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    pattern = "ERROR"

class FilteredTextLogger(FilteredLogger, TextLogger):
    pattern = "ERROR"
# ----------------------------------------------------------------------------------------------