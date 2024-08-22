class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums = [num % value for num in nums]
        freqs = Counter(nums)
        for i, num in enumerate(nums):
            if i % value not in freqs or freqs[i % value] == 0: return i
            freqs[i % value] -= 1
        return len(nums)
 
        
        