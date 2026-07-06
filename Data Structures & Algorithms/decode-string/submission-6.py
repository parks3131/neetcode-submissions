class Solution:
    def decodeString(self, s):
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop() #we are poping [
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                substring = int(k)*substring
                stack.append(substring)
        return "".join(stack)

            

