class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap, ans, next = [], "", None
        for char, freq in Counter(s).items():
            heapq.heappush(max_heap, (-freq, char))

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq += 1
            ans += char
            if next: heapq.heappush(max_heap, next)
            next = (freq, char) if freq < 0 else None
        return ans if not next else ""




        