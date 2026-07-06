class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtracking(open_N,close_N):
            if(open_N == close_N == n):
                res.append("".join(stack))
                return
            if(open_N < n):
                stack.append("(")
                backtracking(open_N+1,close_N)
                stack.pop()
            if(close_N < open_N):
                stack.append(")")
                backtracking(open_N,close_N+1)
                stack.pop()
        backtracking(0,0)
        return res

