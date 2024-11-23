class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = "-" if num < 0 else ""
        ans, num = "", abs(num)
        while num >= 7:
            ans = str(num % 7) + ans
            num //= 7
        return negative + str(num) + ans
        
