class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        r = 0
        write = 0
        while (r < len(chars)):
            curr = chars[r]
            count = 0
            while r < len(chars) and chars[r] == curr:
                count+=1
                r+=1
            chars[write] = curr
            write+=1
            if count>1:
                for i in range(len(str(count))):
                    chars[write] = str(count)[i]
                    write+=1
        return write


