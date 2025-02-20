class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def cost(i, j):
            mid = (i + j) // 2
            return sum(abs(houses[k] - houses[mid]) for k in range(i, j + 1))


        @cache
        def helper(i, k):
            if i == len(houses) and not k: return 0
            if i == len(houses) or not k: return inf
            ans = inf
            for j in range(i, len(houses)):
                ans = min(ans, helper(j + 1, k - 1) + cost(i, j))
            return ans
        
        houses.sort()
        return helper(0, k)
        