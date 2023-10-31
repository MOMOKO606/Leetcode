class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        edges, ans = {}, 0
        for num in nums:
            if num in edges: continue
            left = edges[num - 1] if num - 1 in edges else 0
            right = edges[num + 1] if num + 1 in edges else 0
            edges[num] = edges[num - left] = edges[num + right] = left + 1 + right
            ans = max(ans, edges[num])
        return ans




        