class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, target=target, seq=[]):
            if not target:
                ans.append(seq[:])
                return
            if target < 0 or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                helper(j + 1, target - candidates[j], seq + [candidates[j]])

        ans, candidates = [], sorted(candidates)
        helper()
        return ans
        