class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.nums = [num for row in vec for num in row]
        self.pointer = 0
        

    def next(self) -> int:
        ans = self.nums[self.pointer]
        self.pointer += 1
        return ans
        

    def hasNext(self) -> bool:
        return self.pointer < len(self.nums)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()