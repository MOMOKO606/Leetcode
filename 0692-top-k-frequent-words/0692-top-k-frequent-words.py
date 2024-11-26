class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        return [item[0] for item in sorted(freqs.items(), key=lambda x: (-x[1], x[0]))][:k]
        