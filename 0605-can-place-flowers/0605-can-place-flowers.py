class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, pos in enumerate(flowerbed):
            if pos: continue
            if (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                flowerbed[i], n = 1, n - 1
            
        return n <= 0
        