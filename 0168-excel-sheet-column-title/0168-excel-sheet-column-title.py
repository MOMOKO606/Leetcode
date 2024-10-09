class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans, transfer = "", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while columnNumber:
            columnNumber -= 1
            ans = transfer[columnNumber % 26] + ans
            columnNumber //= 26
        return ans
