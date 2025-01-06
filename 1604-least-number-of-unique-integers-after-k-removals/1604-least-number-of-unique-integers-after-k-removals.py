class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        min_heap = []
        for freq in Counter(arr).values():
            heapq.heappush(min_heap, freq)
        while min_heap and k:
            count = heapq.heappop(min_heap)
            if count > k: return len(min_heap) + 1
            k -= count
        return len(min_heap)
