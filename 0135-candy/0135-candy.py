class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: candies[i] = candies[i - 1] + 1 
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]: candies[j] = max(candies[j], candies[j + 1] + 1) 
        return sum(candies)


        