class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions, ans =  sorted(potions), []
        for num in spells:
            k = bisect.bisect_left(potions, success / num)
            ans.append(len(potions) - k)
        return ans

    
        