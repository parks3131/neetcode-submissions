class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"]":"[", "}":"{", ")":"("}
        stack = []
        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else:
                if stack: 
                    if stack[-1] != hashmap[bracket]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return False if stack else True