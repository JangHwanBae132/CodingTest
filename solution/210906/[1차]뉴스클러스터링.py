import re


def solution(str1, str2):
    answer = 0
    _str1 = str1.lower()
    _str2 = str2.lower()
    A = []
    B = []
    reg = re.compile('[a-z][a-z]')

    for i in range(len(_str1)-1):
        if reg.match(_str1[i:i+2]):
            A.append(_str1[i:i+2])

    for i in range(len(_str2)-1):
        if reg.match(_str2[i:i+2]):
            B.append(_str2[i:i+2])

    if len(A) == 0 and len(B) ==0:
        return 65536
    elif len(A) == 0:
        return 0
    elif len(B) == 0:
        return 0

    # print(A)
    # print(B)
    A_len = len(A)
    B_len = len(B)
    intersect = 0
    union = 0

    for a in A:
        if a in B:
            del B[B.index(a)]
            intersect+=1

    union = A_len+B_len - intersect

    answer = int(intersect/union*65536)

    return answer
