class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, occupied, ans = [], 0, []
        for word in words:
            if len(line) + occupied + len(word) > maxWidth:
                for i in range(maxWidth - occupied):
                    line[i % max((len(line) - 1), 1)] += " "
                ans += ["".join(line)]
                line, occupied = [], 0
            line, occupied = line + [word], occupied + len(word)
        ans.append(" ".join(line).ljust(maxWidth))
        return ans
        

