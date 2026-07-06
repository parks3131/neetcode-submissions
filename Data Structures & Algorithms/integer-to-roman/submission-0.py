class Solution:
    def intToRoman(self, num: int) -> str:
        symbolList = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        res = ""
        for sym, n in symbolList:
            if num//n > 0:
                count = num//n
                res+= sym*count
                num = num%n
        return res