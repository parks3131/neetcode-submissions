import time
class RandomizedSet:
    #so to make all three operation possible in constant time we might need and hash map
    # and an array

    def __init__(self):
        self.hashmap = {}
        self.connector = []

    def insert(self, val: int) -> bool:
        #hash map, array, and linked list can be inserted in O(1)
        #but the catch is if not present in should return True which searching in 
        #O(1) time, so that hash map looks as a good choice
        if val not in self.hashmap:
            self.hashmap[val] = len(self.connector)
            self.connector.append(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        #removing in constant time we can do in hash map
        if val in self.hashmap:
            index = self.hashmap[val]
            self.connector[index] = self.connector[-1]
            self.hashmap[self.connector[-1]] = index
            del self.hashmap[val]
            self.connector.pop()
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        #to getRandom in O(1) it should be in array
        time_in_ns_helper = time.time_ns()%len(self.connector)
        return self.connector[time_in_ns_helper]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()