class DLList:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.head, self.tail = DLList(), DLList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.targets = {}
    
    def add(self, key, value):
        self.tail.key, self.tail.value = key, value
        self.targets[key] = self.tail
        self.tail.next = DLList(prev=self.tail)
        self.tail = self.tail.next

    def delete(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.targets.pop(node.key)


    def get(self, key: int) -> int:
        if key not in self.targets: return -1
        node = self.targets[key]
        value = node.value
        self.delete(node)
        self.add(key, value)
        return value


    def put(self, key: int, value: int) -> None:
        if key in self.targets:
            node = self.targets[key]
            self.delete(node)
        elif not self.size:
            self.delete(self.head.next)
        else:self.size -= 1
        self.add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)