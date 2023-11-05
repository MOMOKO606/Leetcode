class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(num, k, target, seq):
            if not k and not target: 
                ans.append(seq)
                return
            if num > 9 or target < 0: return
            helper(num + 1, k - 1, target - num, seq + [num])
            helper(num + 1, k, target, seq)

        ans = []
        helper(1, k, n, [])
        return ans