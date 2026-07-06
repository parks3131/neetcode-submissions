class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        r, write = 0, 0
        while(r<len(chars)):
            count = 0
            curr = chars[r]
            while ( r<len(chars) and curr == chars[r] ):
                count+=1
                r+=1
            chars[write] = curr
            write+=1
            if count != 1:
                for i in str(count):
                    chars[write] = i
                    write+=1
        return write



