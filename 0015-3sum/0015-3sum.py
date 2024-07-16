class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, ans = sorted(nums), []
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                key = nums[i] + nums[j] + nums[k]
                if key == 0: 
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while i < len(nums) and nums[i] == nums[i - 1]:
                        i += 1
                    j -= 1
                    while j > k and nums[j] == nums[j + 1]:
                        j -= 1
                elif key < 0: i += 1
                else: j -= 1
        return ans



        