class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, target=target, seq=[]):
            if not target: 
                ans.append(seq[:])
                return 
            if target < 0 or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                helper(j, target - candidates[j], seq + [candidates[j]])
        ans = []
        helper()
        return ans
        