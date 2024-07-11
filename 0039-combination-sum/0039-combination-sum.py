
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, target=target, seq=[]):
            if not target: 
                self.ans.append(seq[:])
                return 
            if i > len(candidates) - 1 or target < 0: return 
            helper(i, target - candidates[i], seq + [candidates[i]])
            helper(i + 1, target, seq)
            
        self.ans = []
        helper()
        return self.ans
        
        