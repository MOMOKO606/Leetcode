class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        maxFreq = max(freqs.values())
        k = sum([1 for freq in freqs.values() if freq == maxFreq])
        return max(len(tasks), (maxFreq - 1) * (n + 1) + k) 
        