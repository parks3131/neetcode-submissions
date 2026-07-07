class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        while n != 1:
            Sum = 0
            while n != 0:
                Sum = Sum + pow((n%10),2)
                n = n//10
            n = Sum
            if n in hash_map:
                return False
            hash_map[n] = 1
        return True
