class Solution:
    def minFlips(self, target: str) -> int:
        flipped, count = False, 0
        for char in target:
            if not (char == "0" and not flipped or char == "1" and flipped): 
                count, flipped = count + 1, not flipped
        return count
        