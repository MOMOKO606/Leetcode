class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        trans = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }
        ans = [""]
        for digit in digits:
            ans = [seq + char for char in trans[digit] for seq in ans]
        return ans if digits else []