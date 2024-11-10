class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(remain=k, target=n, seq=[], starter=1):
            if not remain and not target: 
                ans.append(seq)
                return
            if not remain or target <= 0: return
            for i in range(starter, 10):
                helper(remain - 1, target - i, seq + [i], i + 1)

        ans = []
        helper()
        return ans
        