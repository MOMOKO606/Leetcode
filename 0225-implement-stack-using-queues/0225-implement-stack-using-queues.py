class MyStack:

    def __init__(self):
        self.queue = collections.deque([])
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
        

    def top(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        ans = self.queue[0]
        self.queue.append(self.queue.popleft())
        return ans

        

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()