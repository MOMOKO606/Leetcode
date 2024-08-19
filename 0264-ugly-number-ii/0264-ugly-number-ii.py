class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap, visited = [1], set([1])
        for _ in range(n):
            node = heapq.heappop(minHeap)
            for factor in [2, 3, 5]:
                new_node = node * factor 
                if new_node not in visited:
                    visited.add(new_node)
                    heapq.heappush(minHeap, new_node)
        return node

        