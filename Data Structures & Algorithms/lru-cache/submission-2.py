class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key):
        if key not in self.hashmap:
            return -1
        #we should remove it and insert at last with help of right
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])
        return self.hashmap[key].value
    
    def put(self, key, value):
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.insert(self.hashmap[key])
            if len(self.hashmap) > self.capacity:
                lru = self.left.next
                del self.hashmap[lru.key]
                self.remove(lru)
            

        

    
    
    




        
