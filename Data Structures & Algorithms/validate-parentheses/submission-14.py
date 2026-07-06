class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {")" : "(", "]" : "[", "}" : "{" }
        stack = []
        
        for i in s:
            if i not in bracket:
                stack.append(i)
            else:
                if stack:
                    if stack[-1] != bracket[i]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return True if not stack else False
        
            