class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2): s, l = nums1, nums2
        else: s, l = nums2, nums1

        m, n = len(s), len(l)
        low, high = 0, m - 1
        while True:
            mid = (low + high) // 2
            pivot = ceil((m + n) / 2) - mid - 2
            short_mid = s[mid] if mid >= 0 else -inf
            short_mid_next = s[mid + 1] if mid + 1 < m else inf
            long_mid = l[pivot] if pivot >= 0 else -inf
            long_mid_next = l[pivot + 1] if pivot + 1 < n else inf

            if short_mid <= long_mid_next and long_mid <= short_mid_next:
                if (m + n) & 1:
                    return max(short_mid, long_mid)
                else:
                    return (max(short_mid, long_mid) + min(short_mid_next, long_mid_next)) / 2
            elif short_mid > long_mid_next:
                high = mid - 1
            else:
                low = mid + 1
