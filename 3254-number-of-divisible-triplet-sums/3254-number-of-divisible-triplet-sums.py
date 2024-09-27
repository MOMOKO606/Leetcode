class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            visited = collections.defaultdict(int)
            for k in range(i + 1, len(nums)):
                if -nums[k] % d in visited:
                    ans += visited[-nums[k] % d]
                visited[(nums[i] + nums[k]) % d] += 1
        return ans



        