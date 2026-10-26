class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next  = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # left and right are dummy nodes
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    # removes node
    def delete(self, node: Node):
        prev = node.prev
        next = node.next
        # reconnect the 2 nodes
        prev.next = next
        next.prev = prev
    
    # puts node at right side
    def insert(self, node: Node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.insert(node)
            return
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        
