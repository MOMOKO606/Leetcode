class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest, ans = max(candies), []
        for candy in candies:
            if candy + extraCandies >= largest: ans.append(True)
            else: ans.append(False)
        return ans
        