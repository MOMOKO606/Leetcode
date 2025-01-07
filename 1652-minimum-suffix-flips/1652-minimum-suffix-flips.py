class Solution:
    def minFlips(self, target: str) -> int:
        flipped, count = False, 0
        for num in target:
            if (num == "1" and flipped) or (num == "0" and not flipped): continue
            flipped, count = not flipped, count + 1
        return count
        