class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for j in range(0, len(s), 2 * k):
            s[j: j + k] = s[j: j + k][::-1]
        return "".join(s)
        