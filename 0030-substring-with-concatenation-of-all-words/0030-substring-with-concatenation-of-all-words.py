class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        window_length = word_length * len(words)
        target, ans = Counter(words), []
        for i in range(len(s) - window_length + 1):
            seq, temp = s[i: i + window_length], []
            while seq:
                temp.append(seq[:word_length])
                seq = seq[word_length:]
            if Counter(temp) == target: ans.append(i)
        return ans

        