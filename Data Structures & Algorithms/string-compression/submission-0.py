class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        r = 0
        substr = ""
        while (r < len(chars)):
            count = 1
            while r+1 < len(chars) and chars[r] == chars[r+1]:
                count+=1
                r+=1
            if count != 1:
                substr = substr+chars[r]+str(count)
            else:
                substr = substr+chars[r]
            r+=1
        chars[:]=list(substr)
        return len(substr)


