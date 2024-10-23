class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, seq):
            if not left and not right: 
                ans.append(seq)
                return 
            if right > left: helper(left, right - 1, seq + ")")
            if left > 0: helper(left - 1, right, seq + "(") 


        ans = []
        helper(left=n, right=n, seq="")
        return ans
        