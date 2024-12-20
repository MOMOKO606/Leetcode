class Solution:
    def expand(self, s: str) -> List[str]:
        if not s: return [""]
        if s[0].isalpha(): return [s[0] + seq for seq in self.expand(s[1:])]
        if s[0] == "{":
            chars = []
            for i, char in enumerate(s[1:]):
                if char.isalpha(): chars.append(char)
                elif char == "}": break
            return sorted([char + seq for char in chars for seq in self.expand(s[i + 2:])])

        


        