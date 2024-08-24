class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        aux = []
        for num in nums:
            k = bisect.bisect_left(aux, num)
            if k == len(aux): bisect.insort(aux, num)
            else: aux[k] = num
        return len(aux)        