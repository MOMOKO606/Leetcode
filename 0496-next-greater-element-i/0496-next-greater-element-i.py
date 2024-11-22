class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes, ans, stack = {num: i for i, num in enumerate(nums1)}, [-1] * len(nums1), []
        for num in nums2:
            while stack and num > stack[-1]:
                k = indexes.get(stack.pop(), None)
                if k is not None: ans[k] = num
            stack.append(num)
        return ans
        
            
        
        