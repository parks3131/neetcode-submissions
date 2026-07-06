import time
class RandomizedSet:
    #We are using hashtable and array to avoid O(n) time complexity
    #in the random.

    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        self.arr[index] = self.arr[-1]
        self.hashmap[self.arr.pop()] = index
        del self.hashmap[val]
        return True
        
    '''def getRandom(self) -> int:
         return random.choice(self.arr)'''

    def getRandom(self) -> int:
    # use current time in nanoseconds as a "random" seed
        t = time.time_ns()
        index = t % len(self.arr)     # ensures index is within bounds
        return self.arr[index]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()