class SparseVector:
    def __init__(self, nums: List[int]):
        self.indexes = {i: num for i, num in enumerate(nums) if num}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1_indexes = self.indexes
        v2_indexes = vec.indexes
        target, ans = list(set(v1_indexes.keys()).intersection(set(v2_indexes.keys()))), 0
        for i in target:
            ans += v1_indexes[i] * v2_indexes[i]
        return ans


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)