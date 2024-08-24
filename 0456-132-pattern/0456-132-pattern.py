class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, second_largest = [], None
        for num in reversed(nums):
            if second_largest and num < second_largest: return True
            while stack and num > stack[-1]:
                second_largest = stack.pop()
            stack.append(num)
        return False

        