class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet, factor, ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1, 0
        for char in reversed(columnTitle):
            ans += factor * (alphabet.index(char) + 1)
            factor *= 26
        return ans

        