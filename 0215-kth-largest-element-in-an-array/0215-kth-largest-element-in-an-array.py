class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) == k + 1:
                heapq.heappop(minHeap)
        return minHeap[0]
        
        