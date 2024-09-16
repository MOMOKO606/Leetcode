class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            seen = {}
            for k in range(i + 1, len(nums)):
                if -nums[k] % d in seen:
                    ans += seen[-nums[k] % d]
                key = (nums[i] + nums[k]) % d
                seen[key] = seen.get(key, 0) + 1
        return ans

        