class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans, localSum, minHeap = -math.inf, 0, []
        for num1, num2 in sorted(zip(nums1, nums2), key = lambda x: x[1], reverse = True):
            if len(minHeap) + 1 > k:
                num = heapq.heappop(minHeap)
                localSum -= num
            heapq.heappush(minHeap, num1)
            localSum += num1
            if len(minHeap) == k:
                ans = max(ans, localSum * num2)
        return ans

        