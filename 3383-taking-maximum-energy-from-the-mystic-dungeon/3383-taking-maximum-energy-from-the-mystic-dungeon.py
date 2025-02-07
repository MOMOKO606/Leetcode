class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        @cache
        def helper(i):
            if i > len(energy) - k - 1:
                return energy[i]
            return energy[i] + helper(i + k)

        ans = -inf
        for i in range(len(energy)):
            ans = max(ans, helper(i))
        return ans

        