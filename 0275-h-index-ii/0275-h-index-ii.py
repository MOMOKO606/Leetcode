class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations, low, high = citations[::-1], 0, len(citations) - 1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= mid + 1:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1

        