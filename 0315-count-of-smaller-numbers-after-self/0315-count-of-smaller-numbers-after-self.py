class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            nums = []
            while l and r:
                if l[0][0] <= r[0][0]:
                    node = r.pop(0)
                    nums.append(node)
                else:
                    node = l.pop(0)
                    ans[node[1]] += len(r)
                    nums.append(node)
            return nums + (l or r)

        def mergeSort(nums):
            if len(nums) == 1: return nums
            mid = len(nums) // 2
            l, r = mergeSort(nums[:mid]), mergeSort(nums[mid:])
            return merge(l, r)


        ans = [0] * len(nums)
        mergeSort([(num, i) for i, num in enumerate(nums)])
        return ans
        


        
            
        