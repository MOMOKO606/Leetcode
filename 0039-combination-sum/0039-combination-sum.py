class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, seq=[], target=target):
            if not target: 
                ans.append(seq)
                return 
            if target < 0: return
            for j in range(i, len(candidates)):
                helper(j, seq + [candidates[j]], target - candidates[j])
        ans = []
        helper()
        return ans



        