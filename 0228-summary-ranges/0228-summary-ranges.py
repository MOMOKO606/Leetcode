class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        cur_start, cur_end, ans = nums[0], nums[0], []
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] - nums[i - 1] > 1:

                ans += [str(cur_start) + "->" + str(cur_end)] if cur_start != cur_end else [str(cur_start)]
                if i < len(nums): cur_start, cur_end = nums[i], nums[i] 
            else:
                cur_end = nums[i]
        return ans

        