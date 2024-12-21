class FileSystem:

    def __init__(self):
        self.trie = {}
        

    def createPath(self, path: str, value: int) -> bool:
        path, node = path.split("/")[1:], self.trie
        final_file = path[-1]
        for p in path[:-1]:
            if p not in node: return False
            node = node[p]
        if final_file in node: return False
        node[final_file] = {"$": value}
        return True


    def get(self, path: str) -> int:
        node = self.trie
        for p in path.split("/")[1:]:
            if p not in node: return -1
            node = node[p]
        return node["$"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)