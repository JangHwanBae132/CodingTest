import math

def solution(w, h):
    ma = max(w,h)
    mi = min(w,h)
    minus =0
    for i in range(mi):
        minus += math.ceil((i+1)*ma/mi)-math.floor(i*ma/mi)

    answer = w*h-minus
    return answer
