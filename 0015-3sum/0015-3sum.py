class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, ans = sorted(nums), []
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                pivot = nums[k] + nums[i] + nums[j]
                if not pivot: 
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif pivot > 0:
                    j -= 1
                else:
                    i += 1
        return ans
                

