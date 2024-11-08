class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, starter = len(nums), 0
        remain = n
        while remain:
            i, cur = (starter + k) % n, nums[starter]
            while remain:
                nums[i], cur, remain = cur, nums[i], remain - 1
                if i == starter: break
                i = (i + k) % n
            starter += 1
                

