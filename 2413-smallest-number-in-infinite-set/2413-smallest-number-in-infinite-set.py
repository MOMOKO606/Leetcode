class SmallestInfiniteSet:
    def __init__(self):
        self.curSmallest = 1
        self.removed = []

    def getFirstMissing(self):
        nums = self.removed
        for i in range(len(nums)):
            while 0 < nums[i] < len(nums) and (nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]):
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        for i, num in enumerate(nums):
            if i + 1 != num: return i + 1

        return len(nums) + 1
        

    def popSmallest(self) -> int:
        ans = self.curSmallest
        bisect.insort(self.removed, ans)
        self.curSmallest = self.getFirstMissing()
        return ans


    def addBack(self, num: int) -> None:
        if num not in self.removed: return 
        self.removed.remove(num)
        self.curSmallest = self.getFirstMissing()

        
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)