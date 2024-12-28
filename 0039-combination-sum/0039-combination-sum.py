class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, target, seq):
            if not target:
                ans.append(seq)
                return
            if i == len(candidates) or target < 0: return
            helper(i + 1, target, seq)
            helper(i, target - candidates[i], seq + [candidates[i]])


        ans = []
        helper(i=0, target=target, seq=[])
        return ans
        