class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.remain = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        value = self.cache[key]
        self.cache.pop(key)
        self.remain += 1
        self.put(key, value)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.remain += 1
        elif not self.remain:
            self.cache.popitem(last=False)
            self.remain += 1
        self.cache[key] = value
        self.remain -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)