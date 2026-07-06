class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open_parenthesis,close_parenthesis):
            if n == open_parenthesis == close_parenthesis:
                res.append("".join(stack))
                return
            if open_parenthesis < n:
                stack.append("(")
                backtracking(open_parenthesis+1,close_parenthesis)
                stack.pop()
            if close_parenthesis < open_parenthesis:
                stack.append(")")
                backtracking(open_parenthesis,close_parenthesis+1)
                stack.pop()
        backtracking(0,0)
        return res