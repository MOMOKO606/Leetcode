class Logger:

    def __init__(self):
        self.allowed = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.allowed:
            if timestamp < self.allowed[message]: return False
        self.allowed[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)