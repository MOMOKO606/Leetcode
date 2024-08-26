class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, visited, ans = -1, {}, 0
        for j in range(len(s)):
            if s[j] in visited and visited[s[j]] > i:
                i = visited[s[j]]
            visited[s[j]] = j
            ans = max(ans, j - i)
        return ans

        