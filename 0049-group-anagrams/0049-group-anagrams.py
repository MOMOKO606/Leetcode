class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i, word in enumerate(strs):
            key = "".join(sorted(word))
            ans[key] = ans.get(key, []) + [word]
        return [words for key, words in ans.items()]
        