class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_words_length, line, ans = 0, [], []
        for word in words:
            if cur_words_length + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - cur_words_length):
                    line[i % max(len(line) - 1, 1)] += " "
                ans.append("".join(line))
                line, cur_words_length = [], 0
            line, cur_words_length = line + [word], cur_words_length + len(word)
        return ans + [" ".join(line).ljust(maxWidth)]