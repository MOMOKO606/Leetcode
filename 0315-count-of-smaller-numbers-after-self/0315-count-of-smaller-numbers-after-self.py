class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans, sortedNums = [], []
        for num in reversed(nums):
            i = bisect.bisect_left(sortedNums, num)
            bisect.insort(sortedNums, num)
            ans.append(i)
        return ans[::-1]

        