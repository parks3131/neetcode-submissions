class Solution:
    def isValid(self, s: str) -> bool:
        list_parenthesis =[]
        if s == "" or len(s)%2 != 0:
            return False
        for parenthesis in s:
            if parenthesis in ["[","{","("]:
                list_parenthesis.append(parenthesis)
            else:
                if not list_parenthesis:
                    return False
                if list_parenthesis[-1] == "(" and parenthesis == ")":
                    list_parenthesis.pop()
                elif list_parenthesis[-1] == "[" and parenthesis == "]":
                    list_parenthesis.pop()
                elif list_parenthesis[-1] == "{" and parenthesis == "}":
                    list_parenthesis.pop()
                else:
                    return False
        return True if not list_parenthesis else False

            