class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, occupied, ans = [], 0, []
        for word in words:
            if len(line) + occupied + len(word) > maxWidth:
                for i in range(maxWidth - occupied - len(line) + 1):
                    j = i % (len(line) - 1) if len(line) > 1 else 0
                    line[j] += " "
                ans, line, occupied = ans + [" ".join(line)], [], 0
            line, occupied = line + [word], occupied + len(word)
        return ans + [" ".join(line).ljust(maxWidth)]

        