class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node[char] = node.get(char, {})
            node = node[char]
        if "#" not in node: node["#"] = "$"
        

    def search(self, word: str) -> bool:
        def dfsHelper(i=0, node=self.trie):
            if i == len(word): return "#" in node
            if word[i] not in node and word[i] != ".": return False
            if word[i] in node:
                return dfsHelper(i + 1, node[word[i]])
            if word[i] == ".":
                for nextNode in node.values():
                    if not isinstance(nextNode, dict): continue
                    if dfsHelper(i + 1, nextNode): return True
            return False
        return dfsHelper()


            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)