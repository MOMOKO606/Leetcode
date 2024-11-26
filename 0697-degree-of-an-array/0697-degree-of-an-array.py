class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def getIndexFromLeft(target):
            for i, num in enumerate(nums):
                if num == target: return i

        def getIndexFromRight(target):
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == target: return j


        freqs, ans = Counter(nums), len(nums)
        maxFreq = max(freqs.values())
        targets = [key for key, value in freqs.items() if value == maxFreq]
        for target in targets:
            ans = min(ans, getIndexFromRight(target) - getIndexFromLeft(target) + 1)
        return ans
        