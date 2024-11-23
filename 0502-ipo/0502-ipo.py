class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        for p, c in zip(profits, capital):
            heapq.heappush(maxHeap, (-p, c))

        while k and maxHeap:
            available = []
            while maxHeap and w < maxHeap[0][1]:
                available.append(heapq.heappop(maxHeap))
            if maxHeap:
                w -= heapq.heappop(maxHeap)[0]
                k -= 1
                for p, c in available:
                    heapq.heappush(maxHeap, (p, c))
        return w


        