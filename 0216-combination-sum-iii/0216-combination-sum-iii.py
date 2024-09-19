class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k=k, n=n, seq=[], start=1):
            if not n and not k: 
                self.ans.append(seq)
                return 
            if n <= 0 or not k: return
            for num in range(start, 10):
                helper(k - 1, n - num, seq + [num], num + 1)

        
        self.ans = []
        helper()
        return self.ans

        