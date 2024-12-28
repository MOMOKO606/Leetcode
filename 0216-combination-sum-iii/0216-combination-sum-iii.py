class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(target, k, start, seq):
            if not target and not k: 
                ans.append(seq)
                return
            if target <= 0 or not k: return 
            for i in range(start, 10):
                helper(target - i, k - 1, i + 1, seq + [i])



        ans = []
        helper(target=n, k=k, start=1, seq=[])
        return ans
        