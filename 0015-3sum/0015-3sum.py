class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(n=3, pos=0, seq=[], target=0):
            if n == 2:
                i, j = pos, len(nums) - 1
                while i < j:
                    pivot = nums[i] + nums[j]
                    if pivot == target:
                        self.ans.append(seq + [nums[i], nums[j]])
                        i += 1
                        while i < len(nums) and nums[i] == nums[i - 1]:
                            i += 1
                        j -= 1
                        while j >= 0 and nums[j] == nums[j + 1]:
                            j -= 1
                    elif pivot < target:
                        i += 1
                    else:
                        j -= 1
                return
            
            for k in range(pos, len(nums) - n + 1):
                if k > pos and nums[k] == nums[k - 1]: continue
                helper(n - 1, k + 1, seq + [nums[k]], target - nums[k])
        
        nums.sort()
        self.ans = []
        helper()
        return self.ans


                    




        