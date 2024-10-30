class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [[]], {}
        for num in sorted(nums):
            tmp = []
            for seq in ans:
                if num in visited and seq in visited[num]: continue
                visited[num] = visited.get(num, []) + [seq]
                tmp += [[num] + seq]
            ans += tmp
        return ans

        