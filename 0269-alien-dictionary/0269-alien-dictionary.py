class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def dfsHelper(node):
            if node in visited: return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if dfsHelper(neighbor): return True
            visited[node] = False
            self.ans += node


        # Build the graph
        graph = {char: set() for word in words for char in word}
        for word1, word2 in zip(words[:-1], words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    graph[char1].add(char2)
                    break
            else:
                if len(word1) > len(word2): return ""
        
        self.ans, visited = [], {}
        for word in words:
            for char in word:
                if dfsHelper(char): return ""
        return "".join(self.ans[::-1])
        