class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions, ans = sorted([ceil(success / num) for num in potions]), []
        for num in spells:
            ans.append(bisect.bisect_right(potions, num))
        return ans

        