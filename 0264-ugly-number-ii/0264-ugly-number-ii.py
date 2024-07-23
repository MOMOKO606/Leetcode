class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums, p2, p3, p5 = [1], 0, 0, 0
        for i in range(n):
            num = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(num)
            if num == nums[p2] * 2:
                p2 += 1
            if num == nums[p3] * 3:
                p3 += 1
            if num == nums[p5] * 5:
                p5 += 1
        return nums[n - 1]
        
        