class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited, ans = collections.defaultdict(list), [[]]
        for num in sorted(nums):
            tmp = []
            for seq in ans:
                if seq in visited[num]: continue
                tmp += [[num] + seq]
                visited[num] += [seq]
            ans += tmp
        return ans        