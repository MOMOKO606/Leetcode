class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, visited, ans = -1, collections.defaultdict(int), 0
        for j, char in enumerate(s):
            if char in visited and i < visited[char]:
                i = visited[char]
            visited[char] = j
            ans = max(ans, j - i)
        return ans

        
        