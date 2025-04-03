class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap, ans = [], []
        for x, y in queries:
            heapq.heappush(max_heap, -(abs(x) + abs(y)))
            if len(max_heap) > k: heapq.heappop(max_heap)
            if len(max_heap) < k: ans.append(-1)
            else: ans.append(-max_heap[0])
        return ans
            
        