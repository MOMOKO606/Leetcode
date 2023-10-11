class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.Counter(arr)
        return len(freq.values()) == len(set(freq.values()))
        