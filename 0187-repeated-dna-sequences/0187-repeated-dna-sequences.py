class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = {}
        for j in range(len(s) - 9):
            target = s[j: j + 10]
            visited[target] = visited.get(target, 0) + 1
        return [key for key, value in visited.items() if value > 1]
        