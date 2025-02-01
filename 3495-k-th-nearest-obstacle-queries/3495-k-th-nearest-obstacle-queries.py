class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap, ans, heap_size = [], [], 0
        for i, (x, y) in enumerate(queries):
            heapq.heappush(max_heap, -(abs(x) + abs(y)))
            heap_size += 1
            if heap_size > k:
                heapq.heappop(max_heap)
                heap_size -= 1
            if heap_size == k: ans.append(-max_heap[0])
            else: ans.append(-1)
        return ans
        