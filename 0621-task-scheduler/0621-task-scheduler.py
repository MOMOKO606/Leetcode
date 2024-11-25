class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap, ans = [], 0
        for freq in Counter(tasks).values():
            heapq.heappush(maxHeap, -freq)

        while maxHeap:
            count, nextHeap = n + 1, []
            while count:
                if maxHeap: 
                    freq = heapq.heappop(maxHeap) + 1
                    if freq < 0: nextHeap.append(freq)
                count, ans = count - 1, ans + 1
                if not maxHeap and not nextHeap: return ans        
            for freq in nextHeap:
                heapq.heappush(maxHeap, freq)
        return ans



        

        