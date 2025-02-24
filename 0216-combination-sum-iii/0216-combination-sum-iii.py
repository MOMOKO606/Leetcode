class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(i=1, seq=[], k=k, n=n):
            if not n and not k:
                ans.append(seq)
                return ans
            if n <= 0 or not k or i > 9: return 
            helper(i + 1, seq + [i], k - 1, n - i)
            helper(i + 1, seq, k, n)
            

        ans = []
        helper()
        return ans
        