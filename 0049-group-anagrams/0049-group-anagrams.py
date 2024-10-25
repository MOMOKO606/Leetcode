class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            target = "".join(sorted(word))
            ans[target] = ans.get(target, []) + [word]
        return list(ans.values())

        