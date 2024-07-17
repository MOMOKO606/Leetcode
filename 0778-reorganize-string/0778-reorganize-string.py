class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap, no_adjcant, ans = [], [], ""
        for char, freq in Counter(s).items(): heapq.heappush(max_heap, [-freq, char])
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            ans, freq = ans + char, freq + 1
            if no_adjcant:
                next_freq, next_char = no_adjcant.pop()
                heapq.heappush(max_heap, [next_freq, next_char])
            if freq:
                no_adjcant.append([freq, char]) 
        return ans if not no_adjcant else ""


        