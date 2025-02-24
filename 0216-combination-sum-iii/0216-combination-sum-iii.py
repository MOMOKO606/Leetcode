class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(i=1, seq=[], k=k, n=n):
            if not n and not k:
                ans.append(seq)
                return ans
            if n <= 0 or not k: return 
            for j in range(i, 10):
                helper(j + 1, seq + [j], k - 1, n - j)
            

        ans = []
        helper()
        return ans
        