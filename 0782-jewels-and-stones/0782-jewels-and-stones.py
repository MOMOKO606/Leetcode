class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels, ans = set(jewels), 0
        for char in stones:
            if char in jewels: ans += 1
        return ans
        