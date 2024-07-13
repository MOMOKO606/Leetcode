class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(pos=0, target=target, seq=[]):
            if not target: 
                ans.append(seq)
                return
            if target < 0 or pos == len(candidates): return 
            helper(pos, target - candidates[pos], seq + [candidates[pos]])
            helper(pos + 1, target, seq)

        ans = []
        helper()
        return ans        