class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1


        s.reverse()
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == " ": 
                helper(i, j - 1)
                i = j + 1

        