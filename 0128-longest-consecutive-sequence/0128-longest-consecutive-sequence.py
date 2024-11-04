class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet, ans = set(nums), 0
        for num in nums:
            if num - 1 in numSet: continue
            count = 1
            while num + 1 in numSet:
                count, num = count + 1, num + 1
            ans = max(ans, count)
        return ans
        