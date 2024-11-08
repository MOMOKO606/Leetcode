class TwoSum:

    def __init__(self):
        self.nums = []
        

    def add(self, number: int) -> None:
        bisect.insort(self.nums, number)
        

    def find(self, value: int) -> bool:
        i, j = 0, len(self.nums) - 1
        while i < j:
            pivot = self.nums[i] + self.nums[j]
            if pivot == value: return True
            if pivot > value: j -= 1
            else: i += 1
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)