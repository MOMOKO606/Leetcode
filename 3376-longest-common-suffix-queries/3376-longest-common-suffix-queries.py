class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Build the Trie
        trie = {}
        for i, word in enumerate(wordsContainer):
            node, word_length = trie, len(word)
            for char in word[::-1]:
                if "$" not in node or word_length < node["$"][0]: 
                    node["$"] = (word_length, i)
                node[char] = node.get(char, {})
                node = node[char]
            if "$" not in node or word_length < node["$"][0]: 
                node["$"] = (word_length, i)

        ans = []
        for word in wordsQuery:
            node = trie
            for char in word[::-1]:
                if char not in node: break
                node = node[char]
            ans.append(node["$"][1])
        return ans     