class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        visited, i, ans = collections.defaultdict(int), -1, 0
        for j, char in enumerate(s):
            visited[char] += 1
            while len(visited) > 2:
                i += 1
                visited[s[i]] -= 1
                if not visited[s[i]]: visited.pop(s[i])
            ans = max(ans, j - i)
        return ans
            
        