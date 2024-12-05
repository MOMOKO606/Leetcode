class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, num in enumerate(flowerbed):
           if num: continue
           if (i < 1 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]): n, flowerbed[i] = n - 1, 1
        return n <= 0



        