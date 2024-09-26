class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(cur=1, k=k, n=n, seq=[]):
            if not n and not k:
                ans.append(seq[:])
                return
            if not n or not k: return
            for j in range(cur, 10):
                helper(j + 1, k - 1, n - j, seq + [j])

        ans = []
        helper()
        return ans
        