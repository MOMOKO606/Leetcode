class Logger:

    def __init__(self):
        self.logger = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger and self.logger[message] > timestamp:
            return False
        self.logger[message] = timestamp + 10
        return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)