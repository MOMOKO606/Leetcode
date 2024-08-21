class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            reminder = {}
            for j in range(i + 1, len(nums)):
                target = -nums[j] % d
                if target in reminder:
                    ans += reminder[target]
                reminder[(nums[i] + nums[j]) % d] = reminder.get((nums[i] + nums[j]) % d, 0) + 1
        return ans