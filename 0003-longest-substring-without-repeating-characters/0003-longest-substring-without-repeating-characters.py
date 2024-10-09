class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, visited, ans = -1, {}, 0
        for j, char in enumerate(s):
            while char in visited and visited[char] > i:
                i += 1
            visited[char] = j
            ans = max(ans, j - i)
        return ans