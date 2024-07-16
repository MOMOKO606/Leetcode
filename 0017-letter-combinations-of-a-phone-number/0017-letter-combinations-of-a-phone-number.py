class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(i = 0, seq = ""):
            if i == len(digits):
                ans.append(seq[:])
                return 
            for letter in letters[digits[i]]:
                helper(i + 1, seq + letter)
        if digits == "": return []
        ans = []
        letters = {
            "2": "abc", "3": "def", "4": "ghi", 
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz",
            }
        helper()
        return ans 


        

        