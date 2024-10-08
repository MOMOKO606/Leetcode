class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap, visited = [1], set([1])
        for _ in range(n - 1):
            num = heapq.heappop(minHeap)
            for factor in [2, 3, 5]:
                newNum = factor * num
                if newNum not in visited:
                    heapq.heappush(minHeap, newNum)
                    visited.add(newNum)
        return minHeap[0]

        