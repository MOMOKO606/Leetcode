class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfsHelper(i, j, node, seq):
            if "#" in node:
                ans.append(seq)
                node.pop("#")
            if not (0 <= i < rows and 0 <= j < cols and board[i][j] in node): return
            ori = board[i][j]
            board[i][j] = "$"
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                dfsHelper(x, y, node[ori], seq + ori)
            board[i][j] = ori
            if not node[ori]: node.pop(ori)

        # Build the Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node[char] = node.get(char, {})
                node = node[char]
            node["#"] = "#"

        rows, cols, ans = len(board), len(board[0]), []
        for i in range(rows):
            for j in range(cols):
                dfsHelper(i, j, trie, "")
        return ans
        