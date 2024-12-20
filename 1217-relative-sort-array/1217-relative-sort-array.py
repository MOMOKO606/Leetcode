class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqs, rest, ans = {num: 0 for num in arr2}, [], []
        for num in arr1:
            if num in freqs: freqs[num] += 1
            else: bisect.insort(rest, num)
        for num in arr2:
            ans += [num] * freqs[num]
        return ans + rest
        