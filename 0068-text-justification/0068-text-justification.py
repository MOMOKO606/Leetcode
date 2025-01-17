class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        total, line, ans, count = 0, [], [], 0
        for word in words:
            if len(word) + count + total > maxWidth:
                for j in range(maxWidth - total):
                    line[j % max(len(line) - 1, 1)] += " "
                ans, line, total, count = ans + ["".join(line)], [], 0, 0
            line, total, count = line + [word], total + len(word), count + 1
        return ans + [" ".join(line).ljust(maxWidth)]

        