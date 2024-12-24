class FileSystem:

    def __init__(self):
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        path, node, prev = path.split("/")[1:], self.trie, None
        for p in path:
            if p in node:
                node, prev = node[p], p
        if "#" in node: return [prev]
        return sorted(list(node.keys()))


    def mkdir(self, path: str) -> None:
        path, node = path.split("/")[1:], self.trie
        for p in path:
            node[p] = node.get(p, {})
            node = node[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath, node = filePath.split("/")[1:], self.trie
        for p in filePath:
            node[p] = node.get(p, {})
            node = node[p]
        node["#"] = node.get("#", "") + content
        

    def readContentFromFile(self, filePath: str) -> str:
        filePath, node = filePath.split("/")[1:], self.trie
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