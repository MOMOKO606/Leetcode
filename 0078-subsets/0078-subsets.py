class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_sets = [[]]
        for num in nums:
            all_sets += [[num] + s for s in all_sets]
        return all_sets
        