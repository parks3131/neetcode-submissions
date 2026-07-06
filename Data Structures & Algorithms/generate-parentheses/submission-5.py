class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(Open, Close, curr):
            if n == Open == Close:
                res.append("".join(curr))
                return
            
            if Open < n:
                curr.append("(")
                dfs(Open+1, Close, curr)
                curr.pop(-1)

            if Close < Open:
                curr.append(")")
                dfs(Open, Close+1, curr)
                curr.pop(-1)
        dfs(0 ,0 ,curr)
        return res