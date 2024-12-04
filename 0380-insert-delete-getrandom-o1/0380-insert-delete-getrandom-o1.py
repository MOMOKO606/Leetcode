class RandomizedSet:

    def __init__(self):
        self.index = 0
        self.nums = []
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.nums_dict: return False
        self.nums.append(val)
        self.nums_dict[val] = self.index
        self.index += 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.nums_dict: return False
        target = self.nums_dict[val]
        self.nums[target] = self.nums[-1]
        self.nums_dict[self.nums[-1]] = target
        del self.nums_dict[val]
        self.nums.pop()
        self.index -= 1
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()