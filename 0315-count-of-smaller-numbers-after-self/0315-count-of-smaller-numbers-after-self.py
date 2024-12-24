class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums, ans = [], []
        for num in reversed(nums):
            k = bisect.bisect_left(sorted_nums, num)
            ans.append(k)
            bisect.insort(sorted_nums, num)
        return ans[::-1]

        