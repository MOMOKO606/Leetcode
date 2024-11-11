class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return len([value for value in Counter(s).values() if value & 1]) <= 1
        
        