class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indexes, ans = [], []
        for i, num in enumerate(nums):
            if num == x: indexes.append(i)
        for query in queries:
            if query > len(indexes): ans.append(-1)
            else: ans.append(indexes[query - 1])
        return ans

        