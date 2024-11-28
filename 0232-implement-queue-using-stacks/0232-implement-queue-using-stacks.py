class MyQueue:

    def __init__(self):
        self.receive, self.ready = [], []

    def push(self, x: int) -> None:
        self.receive.append(x)
        

    def pop(self) -> int:
        if not self.ready: 
            while self.receive:
                self.ready.append(self.receive.pop())    
        return self.ready.pop()

        

    def peek(self) -> int:
        if not self.ready: 
            while self.receive:
                self.ready.append(self.receive.pop())    
        return self.ready[-1]
        

    def empty(self) -> bool:
        return not self.receive and not self.ready
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()