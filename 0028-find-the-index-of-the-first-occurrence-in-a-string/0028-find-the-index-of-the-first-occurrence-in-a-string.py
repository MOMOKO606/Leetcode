class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(needle=needle):
            next, i = [0], 0
            for j in range(1, len(needle)):
                while i > 0 and needle[j] != needle[i]:
                    i = next[i - 1]
                if needle[j] == needle[i]:
                    next.append(i + 1)
                    i += 1
                else:
                    next.append(0)
            return next

        next, i = getNext(), 0

        for j in range(len(haystack)):
            while i > 0 and haystack[j] != needle[i]:
                i = next[i - 1]
            if haystack[j] == needle[i]:
                i += 1
            if i == len(needle):
                return j - len(needle) + 1
        return -1
        