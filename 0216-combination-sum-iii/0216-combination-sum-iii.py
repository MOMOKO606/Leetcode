class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(start, k, n, seq):
            if not k and not n:
                ans.append(seq[:])
                return 
            if not k or n < 0: 
                return
            for j in range(start, 10):
                helper(j + 1, k - 1, n - j, seq + [j])

        ans = []
        helper(1, k, n, [])
        return ans
            
        