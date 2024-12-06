class FileSystem:

    def __init__(self):
        self.trie = {}
        

    def ls(self, path: str) -> List[str]:
        path = path.split("/")
        path.pop(0)
        node = self.trie
        for p in path:
            if p in node: prev, node = p, node[p]
        return sorted(list(node.keys())) if "#" not in node else [prev]
        

    def mkdir(self, path: str) -> None:
        path = path.split("/")
        path.pop(0)
        node = self.trie
        for p in path:
            node[p] = node.get(p, {})
            node = node[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath = filePath.split("/")
        filePath.pop(0)
        node = self.trie
        for p in filePath:
            node[p] = node.get(p, {})
            node = node[p]
        node["#"] = node.get("#", "") + content

    def readContentFromFile(self, filePath: str) -> str:
        filePath = filePath.split("/")
        filePath.pop(0)
        node = self.trie
        for p in filePath:
            node[p] = node.get(p, {})
            node = node[p]
        return node["#"]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)