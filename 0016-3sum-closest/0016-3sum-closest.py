class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        delta, ans, nums = inf, None, sorted(nums)
        for k in range(len(nums) - 2):
            i, j = k + 1, len(nums) - 1
            while i < j:
                key = nums[k] + nums[i] + nums[j]
                if abs(target - key) < delta:
                    delta = abs(target - key)
                    ans = key
                if key == target: return target
                elif key < target: i += 1
                else: j -= 1
        return ans


        