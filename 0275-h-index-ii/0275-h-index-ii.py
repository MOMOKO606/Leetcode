class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations, left, right = citations[::-1], 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        return left
        