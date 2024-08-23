class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target, i, j, ans = sum(skill) / (len(skill) // 2), 0, len(skill) - 1, 0
        while i < j:
            if skill[i] + skill[j] != target: return -1
            ans += skill[i] * skill[j]
            i, j = i + 1, j - 1
        return ans

        
        