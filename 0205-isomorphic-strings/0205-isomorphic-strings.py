class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transfer = {}
        for char1, char2 in zip(s, t):
            if char1 in transfer:
                if transfer[char1] != char2: return False
            else:
                if char2 in transfer.values(): return False
                transfer[char1] = char2
        return True
        