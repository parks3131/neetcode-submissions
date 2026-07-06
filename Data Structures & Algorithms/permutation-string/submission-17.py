class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we need a want to keep track of the length of the s1 
        #convert s1 into a hashmap
        #l and r to keep track of substring which is permutation

        have = 0
        s1_map = Counter(s1)
        want = len(s1_map)
        hashmap = defaultdict(int)

        l, r = 0, 0
        while r < len(s2):
            if s2[r] in s1_map:
                hashmap[s2[r]]+=1
                if hashmap[s2[r]] == s1_map[s2[r]]:
                    have+=1
                elif hashmap[s2[r]] > s1_map[s2[r]]:
                    while hashmap[s2[r]] > s1_map[s2[r]]:
                        hashmap[s2[l]]-=1
                        have = have-1 if hashmap[s2[l]] == s1_map[s2[l]]-1 else have
                        l+=1

            else:
                hashmap = defaultdict(int)
                have = 0
                l+=1
            if have == want:
                return True
            r+=1
        return False
            

