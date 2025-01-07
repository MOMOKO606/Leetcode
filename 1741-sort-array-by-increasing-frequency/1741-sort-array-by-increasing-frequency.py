class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs, ans = Counter(nums), []
        for num, freq in sorted(freqs.items(), key=lambda x: (x[1], -x[0])):
            ans += [num] * freq
        return ans
        