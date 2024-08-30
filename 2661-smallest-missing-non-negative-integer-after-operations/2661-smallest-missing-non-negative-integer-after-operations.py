class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        reminders = {}
        for num in nums:
            reminder = num % value
            reminders[reminder] = reminders.get(reminder, 0) + 1

        ans = 0
        while True:
            if ans % value not in reminders or not reminders[ans % value]: return ans
            reminders[ans % value] -= 1
            ans += 1
