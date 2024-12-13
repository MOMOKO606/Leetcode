class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap, ans, prev = [], "", None
        for char, freq in Counter(s).items():
            heapq.heappush(max_heap, (-freq, char))
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            ans, freq = ans + char, freq + 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if freq:
                prev = (freq, char)
        return ans if len(ans) == len(s) else ""

        