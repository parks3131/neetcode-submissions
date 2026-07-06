class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_ = {}
        l, curr_length,max_length = 0, 0, 0
        for r in s:
            if r not in hash_:
                hash_[r] = 1
                curr_length+=1
                max_length = max(max_length,curr_length)
            else:
                while(s[l] != r):
                    del hash_[s[l]]
                    curr_length-=1
                    l+=1
                l+=1
        return max_length


            




        