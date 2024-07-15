class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited, i, ans = {}, -1, 0
        for j, char in enumerate(s):
            if char in visited and visited[char] > i:
                i = visited[char]
            visited[char] = j
            ans = max(ans, j - i)
        return ans

        