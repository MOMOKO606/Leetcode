class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, ans = set(), set() 
        for i in range(len(s) - 9):
            seq = s[i: i + 10]
            if seq in visited: ans.add(seq)
            else: visited.add(seq)
        return list(ans)

        