class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Build the Trie
        trie = {}
        for i, word in enumerate(wordsContainer):
            node = trie
            if "$" not in node or len(word) < len(wordsContainer[node["$"]]):
                node["$"] = i
            for char in reversed(word):
                node[char] = node.get(char, {})
                node = node[char]
                if "$" not in node or len(word) < len(wordsContainer[node["$"]]):
                    node["$"] = i
        ans = []
        for word in wordsQuery:
            node = trie
            for char in reversed(word):
                if char not in node: 
                    ans.append(node["$"])
                    break
                node = node[char]
            else:
                ans.append(node["$"])
        return ans