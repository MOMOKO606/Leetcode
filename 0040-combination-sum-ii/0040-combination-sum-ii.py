class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(pos=0, target=target):
            if not target: 
                self.ans.append(seq[:])
                return
            if pos == len(candidates) or target < 0: return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]: continue
                seq.append(candidates[i])
                helper(i + 1, target - candidates[i])
                seq.pop()

        self.ans, candidates, seq = [], sorted(candidates), []
        helper()
        return self.ans
        