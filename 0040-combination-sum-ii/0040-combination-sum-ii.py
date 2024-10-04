class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, seq=[], target=target):
            if not target: 
                ans.append(seq)
                return 
            if target < 0: return 
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                helper(j + 1, seq + [candidates[j]], target - candidates[j])
        
        
        
        candidates, ans = sorted(candidates), []
        helper()
        return ans
        