class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getNext(s):
            i, next = 0, [0]
            for j in range(1, len(s)):
                while i > 0 and s[i] != s[j]:
                    i = next[i - 1]
                if s[i] == s[j]:
                    i += 1
                    next.append(i)
                elif i == 0:
                    next.append(0)
            return next

        backup = s
        s = s + "#" + s[::-1]
        next = getNext(s)
        return backup[next[-1]:][::-1] + backup
                
        