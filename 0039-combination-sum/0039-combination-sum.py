
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, target=target, seq=[]):
            if not target: 
                self.ans.append(seq[:])
                return 
            if i == len(candidates) or target < 0: return 
            for j in range(i, len(candidates)):
                helper(j, target - candidates[j], seq + [candidates[j]])

        self.ans = []
        helper()
        return self.ans
        
        