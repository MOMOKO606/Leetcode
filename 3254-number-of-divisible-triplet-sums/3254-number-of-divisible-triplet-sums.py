class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            reminders = collections.defaultdict(int)
            for k in range(i + 1, len(nums)):
                target = -nums[k] % d
                if target in reminders:
                    ans += reminders[target]
                reminders[(nums[i] + nums[k]) % d] += 1
        return ans

        