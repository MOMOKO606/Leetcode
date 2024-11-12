class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        visited = {}
        s = s.split(" ")
        if len(pattern) != len(s): return False
        for char, word in zip(pattern, s):
            if char not in visited and word not in visited.values():
                visited[char] = word
            elif char in visited and visited[char] != word or char not in visited and word in visited.values(): return False
        return True
        