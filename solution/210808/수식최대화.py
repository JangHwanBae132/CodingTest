import re


def solution(expression):
    answer = []
    numArr, comArr = splitExpression(expression)

    answer.append(cal(numArr, comArr, "+-*" ))
    answer.append(cal(numArr, comArr, "+*-" ))
    answer.append(cal(numArr, comArr, "-+*" ))
    answer.append(cal(numArr, comArr, "-*+" ))
    answer.append(cal(numArr, comArr, "*+-" ))
    answer.append(cal(numArr, comArr, "*-+" ))

    return max(answer)

def splitExpression(expression):
    numArr = re.sub('[^0-9]', " ", expression).split(" ")
    comArr = list(re.sub('[0-9]', "", expression))
    return numArr, comArr

def cal(numArr, comArr, opper):
    newNumArr = numArr.copy()
    newComArr = comArr.copy()
    opList = list(opper)
    for o in opList:
        newNumArr, newComArr= calOpper(newNumArr, newComArr, o)
    return abs(int(newNumArr[0]))


def calOpper(numArr, comArr, o):
    i = 0
    l = len(comArr)
    for j in range(l):
        if o == "+" and comArr[i] == "+":
            v = int(numArr[i]) + int(numArr[i + 1])
            numArr[i]= v
            del numArr[i+1]
            del comArr[i]
        elif o == "-" and comArr[i] == "-":
            v = int(numArr[i]) - int(numArr[i + 1])
            numArr[i]= v
            del numArr[i+1]
            del comArr[i]
        elif o == "*" and comArr[i] == "*":
            v = int(numArr[i]) * int(numArr[i + 1])
            numArr[i]= v
            del numArr[i+1]
            del comArr[i]
        else:
            i += 1
    return numArr, comArr
