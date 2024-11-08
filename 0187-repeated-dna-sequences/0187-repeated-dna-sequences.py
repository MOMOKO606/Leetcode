class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, visited = set([]), set([])
        for i in range(len(s) - 9):
            if s[i: i + 10] in visited: ans.add(s[i: i + 10])
            visited.add(s[i: i + 10])
        return list(ans)
        