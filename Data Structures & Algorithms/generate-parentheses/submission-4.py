class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subsetstack = []
        def validParenthesisSubset(n, opened, closed):
            if n == opened == closed :
                res.append("".join(subsetstack))
                return
            
            if opened < n:
                subsetstack.append("(")
                validParenthesisSubset(n,opened + 1, closed)
                subsetstack.pop(-1)

            if closed < opened:
                subsetstack.append(")")
                validParenthesisSubset(n,opened, closed + 1)
                subsetstack.pop(-1)
        

        validParenthesisSubset(n,0,0)
        return res