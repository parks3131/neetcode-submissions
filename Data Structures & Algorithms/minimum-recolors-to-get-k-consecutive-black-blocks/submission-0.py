class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        white = 0
        for i in range(l,k):
            if blocks[i] == "W":
                white+=1
        length = white
        while r < len(blocks) - 1:
            if blocks[l] == "W":
                length-=1
            r+=1
            l+=1
            if blocks[r] == "W":
                length+=1
            white = min(white, length)
        return white
           
            