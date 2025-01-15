class SmallestInfiniteSet:

    def __init__(self):
        self.iter = 1
        self.min_heap, self.in_heap = [], set([])

    def popSmallest(self) -> int:
        if self.min_heap:
            ans = heapq.heappop(self.min_heap)
            self.in_heap.remove(ans)
        else:
            ans = self.iter
            self.iter += 1
        return ans
        

    def addBack(self, num: int) -> None:
        if num < self.iter and num not in self.in_heap:
            heapq.heappush(self.min_heap, num)
            self.in_heap.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)