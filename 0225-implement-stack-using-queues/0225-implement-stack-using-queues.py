class MyStack:

    def __init__(self):
        self.deque = collections.deque()
        

    def push(self, x: int) -> None:
        self.deque.append(x)
        

    def pop(self) -> int:
        for _ in range(len(self.deque) - 1):
            self.deque.append(self.deque.popleft())
        return self.deque.popleft()
        

    def top(self) -> int:
        return self.deque[-1]
        

    def empty(self) -> bool:
        return not self.deque 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()