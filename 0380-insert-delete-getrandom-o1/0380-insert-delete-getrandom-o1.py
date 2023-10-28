class RandomizedSet:

    def __init__(self):
        self.numsDict, self.numsList = {}, []
        

    def insert(self, val: int) -> bool:
        if val in self.numsDict: return False
        self.numsDict[val] = len(self.numsList)
        self.numsList.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numsDict: return False
        index = self.numsDict[val]
        self.numsDict[self.numsList[-1]] = index
        self.numsList[index] = self.numsList[-1]
        self.numsDict.pop(val)
        self.numsList.pop()
        return True
        

    def getRandom(self) -> int:
        # for key, value in self.numsDict.items():
        #     print(key, value)
        # print(self.numsList)
        return random.choice(self.numsList)
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()