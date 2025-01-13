class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def helper(i=0):
            if i >= len(questions): return 0
            return max(questions[i][0] + helper(i + questions[i][1] + 1), helper(i + 1))
        return helper()
        