class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans, tmp = [], []
        for num in set(nums1):
            if num not in set(nums2): 
                tmp.append(num)
        ans.append(tmp)
        tmp = []
        for num in set(nums2):
            if num not in set(nums1): 
                tmp.append(num)
        ans.append(tmp)
        return ans
            
        