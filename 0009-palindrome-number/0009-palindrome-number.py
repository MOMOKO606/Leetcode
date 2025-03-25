class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        ans, x_copy = 0, x
        while x_copy:
            ans = ans * 10 + x_copy % 10
            x_copy //= 10
        return ans == x
        
        