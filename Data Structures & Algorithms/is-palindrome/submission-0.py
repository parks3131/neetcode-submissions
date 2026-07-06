class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = s.replace(" ","")
        new_string = re.sub(r"[^A-Za-z0-9]","",new_string)
        new_string = new_string.lower()
        return new_string == new_string[::-1]
            
                

