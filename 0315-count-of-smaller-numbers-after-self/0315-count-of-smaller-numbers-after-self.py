class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            sorted_nums = []
            while left and right:
                if left[0][0] > right[0][0]:
                    node = left.pop(0)
                    ans[node[1]] += len(right)
                    sorted_nums.append(node)
                else:
                    sorted_nums.append(right.pop(0))
            return sorted_nums + (left or right)

        def mergeSort(nums):
            n = len(nums)
            if n == 1: return nums
            mid = n // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)

        ans = [0] * len(nums)
        mergeSort([[num, i] for i, num in enumerate(nums)])
        return ans


            
        

        