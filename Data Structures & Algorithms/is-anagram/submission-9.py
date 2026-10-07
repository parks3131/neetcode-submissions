class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hash_map[s[i]]+=1
            hash_map[t[i]]-=1
        for i in range(len(s)):
            if hash_map[s[i]] != 0 or hash_map[t[i]] != 0:
                return False
        return True