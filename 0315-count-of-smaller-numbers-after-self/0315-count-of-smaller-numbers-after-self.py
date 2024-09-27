class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            sorted_nums = []
            while left and right:
                if left[0][0] > right[0][0]:
                    node = left.pop(0)
                    sorted_nums.append(node)
                    self.ans[node[1]] += len(right)
                else:
                    sorted_nums.append(right.pop(0))
            return sorted_nums + (left or right)


        def mergeSort(nums):
            if len(nums) == 1: return nums
            mid = len(nums) // 2
            left, right = mergeSort(nums[:mid]), mergeSort(nums[mid:])
            return merge(left, right)

        self.ans = [0] * len(nums)
        mergeSort([[num, i] for i, num in enumerate(nums)])
        return self.ans
        