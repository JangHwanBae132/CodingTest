import math

def solution(brown, yellow):
    answer = []
    x= ((2+brown/2)+math.sqrt((2+brown/2)*(2+brown/2)-4*(brown+yellow)))/2
    y= 2-x+brown/2
    answer=[x,y]
    return answer
