class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, node):
            if "#" in node: return True
            if  not (0 <= i < rows and 0 <= j < cols and board[i][j] in node): return False
            ori = board[i][j]
            board[i][j] = "$"
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if helper(x, y, node[ori]): return True
            board[i][j] = ori
            

        
        # Build the trie
        trie = node = {}
        for char in word:
            node[char] = node.get(char, {})
            node = node[char]
        node["#"] = "#"
        
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if helper(i, j, trie): return True
        return False
