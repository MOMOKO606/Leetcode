class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def next(nums):
            j = len(nums) - 1
            while j > 0 and nums[j - 1] > nums[j]:
                j -= 1
            i, j = j - 1, len(nums) - 1
            while nums[j] < nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums = nums[:i] + sorted(nums[i:])
            return nums
        
        origin = [i for i in range(1, n + 1)]
        for _ in range(k - 1):
            origin = next(origin)
        return "".join(map(str, origin))
        