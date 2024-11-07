class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.lru = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.lru: return -1
        value = self.lru.pop(key)
        self.lru[key] = value
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.pop(key)
        elif not self.size:
            self.lru.popitem(last=False)
        else:
            self.size -= 1
        self.lru[key] = value
        
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)