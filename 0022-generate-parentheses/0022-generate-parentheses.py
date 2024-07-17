class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left=n, right=n, seq=""):
            if not left and not right: 
                ans.append(seq[:])
                return 
            if right < left or left < 0: return 
            helper(left, right - 1, seq + ")")
            helper(left - 1, right, seq + "(")
        
        ans = []
        helper()
        return ans
        