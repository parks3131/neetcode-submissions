class Node:
    def __init__(self, key, value):
        self.prev, self.next = None, None
        self.key, self.value = key, value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0) 
        self.left.next = self.right
        self.right.prev = self.left
        self.hashmap = {}

    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.next = self.right
        node.prev = temp
        self.right.prev = node
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value    

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
        else:
            self.hashmap[key] = Node(key, value)
            self.insert(self.hashmap[key])
            if self.capacity  < len(self.hashmap):
                lru = self.left.next
                del self.hashmap[lru.key]
                self.remove(lru)
                
            