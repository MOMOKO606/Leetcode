class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        mx = max(map(max, grid))
        pos = [[] for _ in range(mx + 1)]
        for i, row in enumerate(grid):
            for x in set(row):  # 去重
                pos[x].append(i)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return 0
            # 不选 x
            res = dfs(i - 1, j)
            # 枚举选第 k 行的 x
            for k in pos[i]:
                if (j >> k & 1) == 0:
                    res = max(res, dfs(i - 1, j | 1 << k) + i)
            return res
        return dfs(mx, 0)

        
        