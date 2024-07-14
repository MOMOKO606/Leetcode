class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        window_length = word_length * len(words)
        target, ans, wordSet = Counter(words), [], set(words)
        for i in range(len(s) - window_length + 1):
            seq, tmp = s[i: i + window_length], []
            while seq:
                tmp.append(seq[:word_length])
                seq = seq[word_length:]
            if Counter(tmp) == target: ans.append(i)
        return ans

        