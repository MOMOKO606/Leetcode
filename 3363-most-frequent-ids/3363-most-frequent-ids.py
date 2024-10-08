class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        id2freq, maxHeap, ans = {}, [], []
        for id, f in zip(nums, freq):
            id2freq[id] = id2freq.get(id, 0) - f
            heapq.heappush(maxHeap, [id2freq[id], id])
            while maxHeap and maxHeap[0][0] != id2freq[maxHeap[0][1]]:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])
        return ans

        