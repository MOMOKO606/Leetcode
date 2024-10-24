class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(nums):
            count, ans = 1, ""
            for i in range(1, len(nums) + 1):
                if i < len(nums) and nums[i] == nums[i - 1]:
                    count += 1
                else:
                    ans = ans + str(count) + nums[i - 1]
                    count = 1
            return ans

        if n == 1: return "1"
        return rle(self.countAndSay(n - 1))
        