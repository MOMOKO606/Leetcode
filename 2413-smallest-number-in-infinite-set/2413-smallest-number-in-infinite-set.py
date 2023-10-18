class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.addList = []
        self.addSet = set()
        

    def popSmallest(self) -> int:
        if self.addList:
            ans = heapq.heappop(self.addList)
            self.addSet.remove(ans)
        else:
            ans = self.smallest
            self.smallest += 1
        return ans


    def addBack(self, num: int) -> None:
        if num >= self.smallest or num in self.addSet: return
        heapq.heappush(self.addList, num)
        self.addSet.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)