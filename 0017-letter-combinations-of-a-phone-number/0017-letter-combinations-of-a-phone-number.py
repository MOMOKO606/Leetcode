class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digits=digits):
            if digits == "": return [""]
            letters = {
                "2": "abc", "3": "def", "4": "ghi", 
                "5": "jkl", "6": "mno", "7": "pqrs",
                "8": "tuv", "9": "wxyz",
                }
            return [letter + seq for letter in letters[digits[0]] for seq in helper(digits[1:])]
        if digits == "": return []
        return helper()



        

        