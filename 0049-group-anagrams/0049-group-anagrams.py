class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            key = "".join(sorted(word))
            ans[key] = ans.get(key, []) + [word]
        return list(ans.values())

        