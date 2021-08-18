def solution(arr):
    _lcm = 0;
    if len(arr) ==1:
        return arr[0]
    else:
        arr.sort(reverse=True)
        _lcm = lcm(arr[0], arr[1])

    for i in range(2, len(arr)):
        _lcm = lcm(_lcm, arr[i])

    return _lcm

def gcd(a,b):
    while b != 0:
        r = a%b;
        a=b;
        b=r;

    return a

def lcm(a,b):
    return a * b / gcd(a,b)
