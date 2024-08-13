class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, ans, exist_words_length = [], [], 0
        for word in words:
            if exist_words_length + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - exist_words_length):
                    line[i % max(len(line) - 1, 1)] += " "
                ans.append("".join(line))
                line, exist_words_length = [], 0
            line.append(word)
            exist_words_length += len(word)
        return ans + [" ".join(line).ljust(maxWidth)]


            

        