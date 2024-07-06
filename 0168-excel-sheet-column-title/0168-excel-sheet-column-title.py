class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        excel, ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""
        while columnNumber:
            columnNumber -= 1
            ans = excel[columnNumber % 26] + ans
            columnNumber //= 26
        return ans


        