class FileSystem:

    def __init__(self):
        self.trie = {}
        

    def ls(self, path: str) -> List[str]:
        path, node = path.split("/")[1:], self.trie
        if "" in path: path.remove("")
        for p in path:
            node[p] = node.get(p, {})
            prev = p
            node = node[p]
        if "#" in node: 
            return [prev]
        else: return sorted(list(node.keys()))
        

    def mkdir(self, path: str) -> None:
        path, node = path.split("/")[1:], self.trie
        for p in path:
            node[p] = node.get(p, {})
            node = node[p]



    def addContentToFile(self, filePath: str, content: str) -> None:
        path, node = filePath.split("/")[1:], self.trie
        for p in path:
            node[p] = node.get(p, {})
            node = node[p]
        node["#"] = node.get("#", []) + [content]

        

    def readContentFromFile(self, filePath: str) -> str:
        path, node = filePath.split("/")[1:], self.trie
        if "" in path: path.remove("")
        for p in path:
            node[p] = node.get(p, {})
            node = node[p]
        return "".join(node["#"])
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)