class Solution:
    def isValid(self, s: str) -> bool:
        match = {"}":"{","]":"[",")":"("}
        stack = []
        for brac in s:
            if brac not in match:
                stack.append(brac)
            else:
                if stack and match[brac] == stack.pop():
                    continue
                else:
                    return False
        return True if not stack else False