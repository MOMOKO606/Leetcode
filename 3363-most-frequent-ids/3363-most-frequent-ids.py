class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans, freqs, max_heap = [], {}, []
        for id, f in zip(nums, freq):
            freqs[id] = freqs.get(id, 0) + f
            heapq.heappush(max_heap, (-freqs[id], id))
            while max_heap and -max_heap[0][0] != freqs[max_heap[0][1]]:
                heapq.heappop(max_heap)
            ans += [-max_heap[0][0]] if max_heap else [0]
        return ans

        