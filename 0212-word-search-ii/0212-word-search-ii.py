class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs_helper(i, j, seq, node):
            if "#" in node: 
                self.ans.append(seq[:])
                del node["#"]
            if not (0 <= i < rows and 0 <= j < cols and board[i][j] in node): return
            ori = board[i][j]
            board[i][j] = "$"
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                dfs_helper(x, y, seq + ori, node[ori])
            board[i][j] = ori
            if not node[ori]: del node[ori]
            
        
        # Build the trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node[char] = node.get(char, {})
                node = node[char]
            node["#"] = "#"

        rows, cols, self.ans = len(board), len(board[0]), []
        for i in range(rows):
            for j in range(cols):
                dfs_helper(i, j, "", trie)
        return self.ans
        