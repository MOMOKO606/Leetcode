class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for j in range(cols - 2, -1, -1):
            dungeon[rows - 1][j] = max(1, dungeon[rows - 1][j + 1] - dungeon[rows - 1][j])
        for i in range(rows - 2, -1, -1):
            dungeon[i][cols - 1] = max(1, dungeon[i + 1][cols - 1] - dungeon[i][cols - 1])
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i + 1][j] - dungeon[i][j], dungeon[i][j + 1] - dungeon[i][j]))
        return dungeon[0][0]
        