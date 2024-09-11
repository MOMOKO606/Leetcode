class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, target=target):
            if target < 0 or i == len(candidates): return
            if not target:
                self.ans.append(seq[:])
                return 
            for j in range(i, len(candidates)):
                seq.append(candidates[j])
                helper(j, target - candidates[j])
                seq.pop()

        self.ans, seq = [], []
        helper()
        return self.ans
        