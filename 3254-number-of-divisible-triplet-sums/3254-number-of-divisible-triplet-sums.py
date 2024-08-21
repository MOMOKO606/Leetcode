class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            reminders = {}
            for j in range(i + 1, len(nums)):
                if -nums[j] % d in reminders: ans += reminders[-nums[j] % d]
                reminders[(nums[i] + nums[j]) % d] = reminders.get((nums[i] + nums[j]) % d, 0) + 1
        return ans

        