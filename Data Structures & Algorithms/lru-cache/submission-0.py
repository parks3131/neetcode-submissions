class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_key = {}
        self.least_recent = []
    

    def get(self, key: int) -> int:
        if key not in self.hash_key:
            return -1
        self.least_recent.remove(key)
        self.least_recent.append(key)
        return self.hash_key[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_key:
            self.hash_key[key] = value
            self.least_recent.remove(key)
            self.least_recent.append(key)
        else:
            if len(self.hash_key) == self.capacity:
                lru = self.least_recent.pop(0)
                del self.hash_key[lru]
            self.hash_key[key] = value
            self.least_recent.append(key)
            


        




#if the pair not exist pop the last element get and put in O(1)
