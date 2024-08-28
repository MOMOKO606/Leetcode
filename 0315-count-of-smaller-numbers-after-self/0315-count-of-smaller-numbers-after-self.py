class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            nums = []
            while left and right:
                if left[0][0] > right[0][0]:
                    ans[left[0][1]] += len(right)
                    nums.append(left.pop(0))
                else:
                    nums.append(right.pop(0))
            nums += left or right
            return nums
            
        def mergeSort(nums):
            if len(nums) == 1: return nums
            mid = len(nums) // 2
            left, right = mergeSort(nums[:mid]), mergeSort(nums[mid:])
            return merge(left, right)

        ans = [0] * len(nums)
        mergeSort([(num, i) for i, num in enumerate(nums)])
        return ans
        