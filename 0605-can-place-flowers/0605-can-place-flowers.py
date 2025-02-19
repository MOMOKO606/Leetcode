class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        for i, num in enumerate(flowerbed):
            if num: continue
            if (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]): n, flowerbed[i] = n - 1, 1
            if not n: return True
        return False
        