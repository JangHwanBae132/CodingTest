import math


def solution(n,a,b):
    height = int(math.log2(n))
    for i in range(height):
        a_quotient = int((a-1)/(n/2))
        b_quotient = int((b-1)/(n/2))
        if a_quotient == b_quotient:
            a = a-a_quotient*(n/2)
            b = b-b_quotient*(n/2)
            n = n/2
        else:
            return height-i
