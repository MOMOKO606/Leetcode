class DLListNode:
    def __init__(self, prev=None, next=None, key=0, value=0):
        self.prev, self.next, self.key, self.value = prev, next, key, value

class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = DLListNode(), DLListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.remain = capacity
        self.keys = {}

    def add(self, key: int, value: int) -> DLListNode:
        self.tail.key, self.tail.value = key, value
        self.tail.next = DLListNode(prev = self.tail)
        node = self.tail
        self.tail = self.tail.next
        self.keys[key] = node
        self.remain -= 1
        return node

    def remove(self, node: DLListNode) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.remain += 1
        self.keys.pop(node.key)

    def get(self, key: int) -> int:
        if key not in self.keys: return -1
        cur_node = self.keys[key]
        self.put(key, cur_node.value)
        return cur_node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            cur_node = self.keys[key]
            self.remove(cur_node)
        elif not self.remain:
            self.remove(self.head.next)
        new_node = self.add(key, value)
        self.keys[key] = new_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)