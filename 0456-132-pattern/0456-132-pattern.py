class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, secondLargest = [], None
        for num in reversed(nums):
            while stack and num > stack[-1]:
                secondLargest = stack.pop()
            stack.append(num)
            if secondLargest and num < secondLargest: return True
        return False
        