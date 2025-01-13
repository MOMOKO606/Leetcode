class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums1, nums2, ans = sorted([nums[i] for i in range(0, len(nums), 2)]), sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True), []
        while nums1 and nums2:
            ans.append(nums1.pop(0))
            ans.append(nums2.pop(0))
        ans += (nums1 or nums2)
        return ans
        