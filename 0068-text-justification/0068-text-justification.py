class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_words_length, line, ans = 0, [], []
        for word in words:
            if cur_words_length + len(line) + len(word) > maxWidth:
                remain_spaces = maxWidth - cur_words_length
                for i in range(remain_spaces):
                    line[i % max(len(line) - 1, 1)] += " "
                ans.append("".join(line))
                cur_words_length, line = 0, []
            line.append(word)
            cur_words_length += len(word)
        ans.append(" ".join(line).ljust(maxWidth))
        return ans


        