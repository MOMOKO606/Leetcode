class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            nums = []
            while left and right:
                if left[0][1] > right[0][1]:
                    ans[left[0][0]] += len(right)
                    nums.append(left.pop(0))
                else:
                    nums.append(right.pop(0))
            return nums + (left or right)
        
        
        def merge_sort(nums):
            if len(nums) <= 1: return nums
            n = len(nums) // 2
            left = merge_sort(nums[:n])
            right = merge_sort(nums[n:])
            return merge(left, right)

        ans = [0] * len(nums)
        merge_sort([[i, num] for i, num in enumerate(nums)])
        return ans
        