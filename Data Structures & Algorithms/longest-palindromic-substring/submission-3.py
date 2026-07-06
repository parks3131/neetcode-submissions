class Solution:
    def longestPalindrome(self, s: str) -> str:
        #we are gonna assume each element as center and then
        #spread on both way untill l and r are equal
        #also make sure that we will make assumption in two ways
        #first as a even and second as a odd string
        #we store it in a longestPalindrome if the length is larger
        #than the previous
        longestPalindrome = ""
        length = 0

        for i in range(len(s)):
            dummyPalindrome = ""
            #Consider as odd
            l, r = i, i
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if length < r - l + 1:
                longestPalindrome = s[l+1:r]
                length = r - l + 1
            #Consider as even
            l, r = i, i + 1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if length < r - l + 1:
                longestPalindrome = s[l+1:r]
                length = r - l + 1
        return longestPalindrome

        