class FileSystem:

    def __init__(self):
        self.trie = {}
        

    def ls(self, path: str) -> List[str]:
        path, node, prev = path.split("/")[1:], self.trie, None
        for char in path:
            if not char: continue
            prev = char
            node = node[char]
        return sorted(list(node.keys())) if "#" not in node else [char]


    def mkdir(self, path: str) -> None:
        path, node = path.split("/")[1:], self.trie
        for char in path:
            node[char] = node.get(char, {})
            node = node[char]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath, node = filePath.split("/")[1:], self.trie
        for char in filePath:
            node[char] = node.get(char, {})
            node = node[char]
        node["#"] = node.get("#", "") + content

        

    def readContentFromFile(self, filePath: str) -> str:
        filePath, node = filePath.split("/")[1:], self.trie
        for char in filePath:
            node = node[char]
        return node["#"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)