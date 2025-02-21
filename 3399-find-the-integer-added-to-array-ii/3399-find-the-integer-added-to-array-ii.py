class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        def is_valid(delta):
            i = j = count = 0
            while i < len(nums1) and j < len(nums2):
                if nums2[j] - nums1[i] != delta:
                    count += 1
                else:
                    j += 1
                i += 1
            return count <= 2 



        nums1.sort()
        nums2.sort()
        ans = inf
        for i in range(3):
            delta = nums2[0] - nums1[i]
            if is_valid(delta):
                ans = min(ans, delta)
        return ans
        
        