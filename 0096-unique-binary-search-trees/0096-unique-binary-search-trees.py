class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def helper(l, r):
            if l >= r: return 1
            ans = 0
            for k in range(l, r + 1):
                ans += helper(l, k - 1) * helper(k + 1, r)
            return ans

        return helper(1, n)
        
        