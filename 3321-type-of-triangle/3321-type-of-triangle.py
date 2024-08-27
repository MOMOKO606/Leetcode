class Solution:
    def triangleType(self, nums: List[int]) -> str:
       a, b, c = sorted(nums)
       if a + b <= c: return "none"
       elif a == b == c: return "equilateral"
       elif a != b != c: return "scalene"
       else: return "isosceles"

        