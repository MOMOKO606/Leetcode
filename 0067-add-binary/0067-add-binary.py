class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry, ans = len(a) - 1, len(b) - 1, 0, []
        while i >= 0 or j >= 0 or carry:
            if i >= 0: carry += int(a[i]) 
            if j >= 0: carry += int(b[j])
            ans.append(carry % 2)
            carry = 1 if carry > 1 else 0
            i, j = i - 1, j - 1
        return "".join(map(str, ans[::-1]))


    
        