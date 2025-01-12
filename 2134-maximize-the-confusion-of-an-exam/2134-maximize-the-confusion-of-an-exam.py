class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ts, fs, i, ans = 0, 0, -1, -inf
        for j, char in enumerate(answerKey):
            if char == "T": ts += 1
            else: fs += 1

            while max(ts, fs) + k < j - i:
                i += 1
                if answerKey[i] == "T": ts -= 1
                else: fs -= 1
            ans = max(ans, j - i)
        return ans
        