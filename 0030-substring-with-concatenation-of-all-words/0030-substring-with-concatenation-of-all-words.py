class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        window_length = word_length * len(words)
        target, ans = Counter(words), []
        for i in range(len(s) - window_length + 1):
            seq = []
            for j in range(i, i + window_length, word_length):
                tmp = s[j: j + word_length]
                if tmp not in words: break
                seq.append(tmp)
            if Counter(seq) == target: ans.append(i)
        return ans

        