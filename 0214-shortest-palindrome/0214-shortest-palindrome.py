class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_next(s):
            next, i = [0], 0
            for j in range(1, len(s)):
                while i > 0 and s[j] != s[i]:
                    i = next[i - 1]
                if s[i] == s[j]: 
                    i += 1
                    next.append(i)
                else:
                    next.append(0)
            return next

        next = get_next(s + "#" + s[::-1])
        i = next[-1]
        return s[i:][::-1] + s
        