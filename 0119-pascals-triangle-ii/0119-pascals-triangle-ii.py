class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = [1]
        for _ in range(rowIndex):
            tmp = [line[j - 1] + line[j] for j in range(1, len(line))]
            line = [1] + tmp + [1]
        return line

        