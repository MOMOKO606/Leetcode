class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next(needle):
            next, i = [0], 0
            for j in range(1, len(needle)):
                while i > 0 and needle[i] != needle[j]:
                    i = next[i - 1]
                if needle[i] != needle[j]:
                    next.append(0)
                else:
                    i += 1
                    next.append(i)
            return next

        
        next, i = get_next(needle), 0
        for j in range(len(haystack)):
            while i > 0 and haystack[j] != needle[i]:
                i = next[i - 1]
            if haystack[j] == needle[i]: 
                i += 1
            if i == len(needle):
                return j - len(needle) + 1
        return -1
            
        