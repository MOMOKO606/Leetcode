class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, seq=[], target=target):
            if not target: 
                ans.append(seq)
                return
            if target < 0 or i == len(candidates):
                return
            helper(i, seq + [candidates[i]], target - candidates[i])
            helper(i + 1, seq, target)

        ans = []
        helper()
        return ans
        