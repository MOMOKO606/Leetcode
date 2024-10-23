class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(n, i, seq):
            prev_sum = sum(seq)
            if n == 2:
                l, r = i, len(nums) - 1
                while l < r:
                    pivot = prev_sum + nums[l] + nums[r]
                    if pivot == target:
                        ans.append(seq + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif pivot < target:
                        l += 1
                    else:
                        r -= 1
                return
            for j in range(i, len(nums) - n + 1):
                if j > i and nums[j] == nums[j - 1]: continue
                nSum(n - 1, j + 1, seq + [nums[j]])

        nums, ans = sorted(nums), []
        nSum(4, 0, [])
        return ans

            
        