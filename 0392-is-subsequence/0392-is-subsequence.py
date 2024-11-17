class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = collections.deque(list(s))
        for char in t:
            if not s: return True
            if char == s[0]: 
                s.popleft()
        return not s
        