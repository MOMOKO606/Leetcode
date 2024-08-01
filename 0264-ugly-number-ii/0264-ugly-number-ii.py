class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums, p2, p3, p5 = [1], 0, 0, 0
        while n - 1:
            target = min(2 * nums[p2], 3 * nums[p3], 5 * nums[p5])
            if 2 * nums[p2] == target:
                p2 += 1
            if 3 * nums[p3] == target:
                p3 += 1
            if 5 * nums[p5] == target:
                p5 += 1
            nums.append(target)
            n -= 1
        return nums[-1]

 
        