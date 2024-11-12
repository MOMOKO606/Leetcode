class MedianFinder:

    def __init__(self):
        self.maxHeap, self.count1 = [], 0
        self.minHeap, self.count2 = [], 0
        

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]: 
            heapq.heappush(self.minHeap, num)
            self.count2 += 1
        else: 
            heapq.heappush(self.maxHeap, -num)
            self.count1 += 1

        if self.count2 > self.count1:
            node = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -node)
            self.count2 -= 1
            self.count1 += 1
        if self.count1 - self.count2 > 1:
            node = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, node)
            self.count1 -= 1
            self.count2 += 1


    def findMedian(self) -> float:
        if (self.count1 + self.count2) & 1: return -self.maxHeap[0]
        else: return (self.minHeap[0] - self.maxHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()