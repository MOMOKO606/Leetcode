class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2): s, l = nums1, nums2
        else: s, l = nums2, nums1
        
        m, n, low, high = len(s), len(l), 0, len(s) - 1
        while True:
            s_mid = math.floor((low + high) / 2)
            l_mid = math.ceil((m + n) / 2) - s_mid - 2
            s_median = s[s_mid] if s_mid >= 0 else -inf
            s_median_next = s[s_mid + 1] if s_mid + 1 < m else inf
            l_median = l[l_mid] if l_mid >= 0 else -inf
            l_median_next = l[l_mid + 1] if l_mid + 1 < n else inf
            if s_median <= l_median_next and l_median <= s_median_next:
                if (m + n) & 1: return max(s_median, l_median) 
                else: return (max(s_median, l_median) + min(s_median_next, l_median_next)) / 2.0
            elif s_median >l_median_next:
                high = s_mid - 1
            else:
                low = s_mid + 1



        