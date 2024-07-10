class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, visited = [], set()
        for i in range(len(s) - 9):
            seq = s[i: i + 10]
            if seq not in visited: 
                visited.add(seq)
                if s.find(seq, i + 1, len(s)) != -1: 
                    ans.append(seq)
                    continue
        return ans

        