class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Build the Trie
        trie = {}
        for i, word in enumerate(wordsContainer):
            node = trie
            for char in word[::-1]:
                if "$" not in node or len(word) < node["$"][0]: node["$"] = [len(word), i]
                node[char] = node.get(char, {})
                node = node[char]
            if "$" not in node or len(word) < node["$"][0]: node["$"] = [len(word), i]
        
        ans = []
        for word in wordsQuery:
            node = trie
            for char in word[::-1]:
                if char in node: 
                    node = node[char]
                else: 
                    ans.append(node["$"][1])
                    break
            else:
                ans.append(node["$"][1])
        return ans


        