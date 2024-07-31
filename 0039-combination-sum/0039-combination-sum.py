class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, seq=[], target=target):
            if not target:
                ans.append(seq[:])
                return 
            if i == len(candidates) or target < 0: return
            helper(i + 1, seq, target)
            helper(i, seq + [candidates[i]], target - candidates[i])

        ans = []
        helper()
        return ans
        