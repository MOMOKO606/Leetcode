class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freqs, ans, max_freq = collections.defaultdict(int), len(word) // k, -inf
        for i in range(0, len(word) - k + 1, k):
            freqs[word[i: i + k]] += 1
            max_freq = max(max_freq, freqs[word[i: i + k]])
        return ans - max_freq


        
        