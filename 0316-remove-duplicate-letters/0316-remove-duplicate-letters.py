class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indexes, exists, ans = {char: i for i, char in enumerate(s)}, set(), []
        for i, char in enumerate(s):
            if char in exists: continue
            while ans and char < ans[-1] and indexes[ans[-1]] > i:
                exists.remove(ans.pop())
            ans.append(char)
            exists.add(char)
        return "".join(ans)
        
        