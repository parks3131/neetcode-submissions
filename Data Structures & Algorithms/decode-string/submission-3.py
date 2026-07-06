class Solution:
    def decodeString(self, s: str) -> str:
        #i feel like using a stack
        #push elements until i see ]
        #then see the int and multiply accordingly and add it to the stack again
        #then do the same 

        stack = []
        for i in s:
            if i == "]":
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop() #we are poping the [
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substring)
            else:
                stack.append(i)
        return "".join(stack)