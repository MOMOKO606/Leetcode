class Solution:
    def compress(self, chars: List[str]) -> int:
        k, i = 0, 0
        for j in range(len(chars) + 1):
            if j == len(chars) or chars[j] != chars[i]:
                chars[k], k = chars[i], k + 1
                if j - i > 1:
                    chars[k: k + len(str(j - i))] = str(j - i)
                    k = k + len(str(j - i))
                i = j
        return k
        