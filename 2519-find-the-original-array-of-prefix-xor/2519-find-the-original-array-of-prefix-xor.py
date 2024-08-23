class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        for i in range(len(pref) - 1, 0, -1):
            ans.append(pref[i] ^ pref[i - 1])
        ans.append(pref[0])
        return ans[::-1]

        