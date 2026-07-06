class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop() #poping [
                numstring = ""
                while stack and stack[-1].isdigit():
                    numstring = stack.pop()+numstring
                stack.append(int(numstring)*substring)
        return "".join(stack)
            
            

