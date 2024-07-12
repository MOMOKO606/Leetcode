class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        freqs, maxHeap, ans = {}, [], []
        for id, f in zip(nums, freq):
            freqs[id] = freqs.get(id, 0) + f
            heapq.heappush(maxHeap, (-freqs[id], id))
            while maxHeap and -maxHeap[0][0] != freqs[maxHeap[0][1]]:
                heapq.heappop(maxHeap)
            ans += [-maxHeap[0][0]] if maxHeap else [0]
        return ans


        