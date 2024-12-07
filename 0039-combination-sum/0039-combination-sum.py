class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, target, seq):
            if not target: 
                ans.append(seq[:])
                return 
            if target < 0 or i == len(candidates): return
            helper(i, target - candidates[i], seq + [candidates[i]])
            helper(i + 1, target, seq)


        ans = []
        helper(i=0, target=target, seq=[])
        return ans
        