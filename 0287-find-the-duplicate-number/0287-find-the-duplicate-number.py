class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        slow = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if slow == fast: return slow