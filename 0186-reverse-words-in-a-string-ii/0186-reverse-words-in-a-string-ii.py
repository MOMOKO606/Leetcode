class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        reverse(0, len(s) - 1)
        i = -1
        for j in range(len(s)):
            if s[j] == " ": 
                reverse(i + 1, j - 1)
                i = j
        reverse(i + 1, len(s) - 1)


        