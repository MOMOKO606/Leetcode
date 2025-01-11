class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        def update(i, j, stones):
            n = j - i - 1
            row[i + 1: j - stones] = ["."] * (n - stones)
            row[j - stones: j] = ["#"] * stones

        for row in boxGrid:
            j, stones = len(row), 0
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "*":
                    update(i, j, stones)
                    j, stones = i, 0
                elif row[i] == "#":
                    stones += 1
            update(-1, j, stones)
        
        rows, cols = len(boxGrid), len(boxGrid[0])
        ans = []
        for j in range(cols):
            ans.append([boxGrid[i][j] for i in range(rows - 1, -1, -1)])
        return ans

        