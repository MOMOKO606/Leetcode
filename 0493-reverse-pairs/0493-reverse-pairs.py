class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l, r):
            i, j, ans = 0, 0, []
            while i < len(l) and j < len(r):
                if l[i] > 2 * r[j]: self.ans, j = self.ans + len(l) - i, j + 1
                else: i += 1
            while l and r:
                if l[0] < r[0]:
                    ans.append(l.pop(0))
                else:
                    ans.append(r.pop(0))
            ans += (l or r)
            return ans
            
        def mergeSort(nums):
            if len(nums) == 1: return nums
            mid = len(nums) // 2
            l = mergeSort(nums[:mid])
            r = mergeSort(nums[mid:])
            return merge(l, r)

        self.ans = 0
        mergeSort(nums)
        return self.ans