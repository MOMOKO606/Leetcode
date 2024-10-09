class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(i=0):
            if i == len(digits): return [""]
            return [char + seq for char in transfer[digits[i]] for seq in helper(i + 1)]

        transfer = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        return helper() if digits else []
        
        


        