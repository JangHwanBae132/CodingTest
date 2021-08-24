def solution(numbers):
    answer = ''

    sort = quick_sort(numbers)
    if(sort[0]=='0'):
        return '0'

    for s in sort:
        answer+=s

    return answer


def quick_sort(_numbers):
    if len(_numbers) <= 1:
        return _numbers
    pivot = str(_numbers[0])

    greater_arr, lesser_arr, equal_arr = [], [], []

    for num in _numbers:
        if int(str(num) + pivot) > int(pivot + str(num)):
            greater_arr.append(str(num))
        elif int(str(num) + pivot) < int(pivot + str(num)):
            lesser_arr.append(str(num))
        else:
            equal_arr.append(str(num))

    return quick_sort(greater_arr) + equal_arr + quick_sort(lesser_arr)
