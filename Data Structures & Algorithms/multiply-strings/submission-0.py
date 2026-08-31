class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #we are not supposed to convert these char or strings to numbers
        answerList = [0]*(len(num1) + len(num2)) # the multiplication might be in length of atmost the digits sum of two eg 99*99 gives four digit number
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                answerList[i + j]+= int(num1[i])*int(num2[j])
                answerList[i + j + 1]+= answerList[i + j]//10     #mul of two one digit 9*9 max is 81
                answerList[i + j] = answerList[i + j]%10
        
        res = answerList[::-1]
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1
        return "".join(map(str, res[i:]))