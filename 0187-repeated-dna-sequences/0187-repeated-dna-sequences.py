class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, ans = set(), set()
        for j in range(len(s)):
            if j >= 9:
                i = j - 9
                if s[i:j + 1] in visited: ans.add(s[i: j + 1])
                else: visited.add(s[i: j + 1])
        return list(ans)
        