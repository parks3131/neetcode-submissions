class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        want_hash = Counter(t)
        have_hash = defaultdict(int)
        want = len(want_hash)
        have = 0
        l, r = 0, 0
        length = float("inf")
        result = ""
        while r < len(s):
            if s[r] in want_hash:
                have_hash[s[r]]+=1
                have = have + 1 if have_hash[s[r]] == want_hash[s[r]] else have
            while have == want:
                if length > r - l + 1:
                    length = r - l + 1
                    result = s[l:r + 1]
                if s[l] in want_hash:
                    have_hash[s[l]]-=1
                    have = have - 1 if have_hash[s[l]] < want_hash[s[l]] else have
                l+=1
            r+=1
        return result

        
