class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet, ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""
        while columnNumber:
            columnNumber -= 1
            ans = alphabet[columnNumber % 26] + ans
            columnNumber //= 26
        return ans

        