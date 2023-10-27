class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations, ans = sorted(citations, reverse = True), 0
        for i, num in enumerate(citations):
            ans = max(ans, min(num, i + 1))
        return ans

        