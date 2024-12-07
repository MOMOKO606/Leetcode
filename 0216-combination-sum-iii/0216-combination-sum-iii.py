class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, i, seq):
            if not n and not k:
                ans.append(seq)
                return 
            if not n or not k: return
            for j in range(i, 10):
                helper(k - 1, n - j, j + 1, seq + [j])


        ans = []
        helper(k=k, n=n, i=1, seq=[])
        return ans
        