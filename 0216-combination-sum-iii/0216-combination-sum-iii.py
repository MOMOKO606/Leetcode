class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, i, seq):
            if not k and not n: 
                ans.append(seq)
                return
            if not k or not n or i >= len(data): return
            helper(k, n, i + 1, seq)
            helper(k - 1, n - data[i], i + 1, seq + [data[i]])


        ans, data = [], [1, 2, 3, 4, 5, 6, 7, 8, 9]
        helper(k, n, 0, [])
        return ans
        