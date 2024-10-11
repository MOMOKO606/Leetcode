class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        trans = {}
        for key, value in zip(s, t):
            if key not in trans.keys() and value not in trans.values(): trans[key] = value
            elif key not in trans.keys() or trans[key] != value: return False
        return True
        