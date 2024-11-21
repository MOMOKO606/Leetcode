class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def helper(i=0, m=m, n=n):
            if m < 0 or n < 0: return -inf
            if (not m and not n) or i == len(strs): return 0
            
            zeros, ones = strs[i].count("0"), strs[i].count("1")
            return max(helper(i + 1, m - zeros, n - ones) + 1, helper(i + 1, m, n))
        ans = helper()
        return ans if ans != -inf else 0
