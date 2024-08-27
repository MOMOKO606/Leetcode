class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        pivot, nums = len(nums) // 2, sorted(nums)
        ans = abs(nums[pivot] - k)
        for j in range(pivot + 1, len(nums)):
            if nums[j] < k: 
                ans += k - nums[j] 
            else: break
        for i in range(pivot - 1, -1, -1):
            if nums[i] > k:
                ans += nums[i] - k
            else: break
        return ans


        


        