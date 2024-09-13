class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet, ans = set(nums), 0
        for num in nums:
            if num - 1 in numSet: continue
            end = num
            while end + 1 in numSet:
                end += 1
            ans = max(ans, end - num + 1)
        return ans
        