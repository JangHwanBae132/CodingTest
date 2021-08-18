import re

def solution(files):
    # \d{,5} 이거는 없는 것도 찾아서 ''를 넣어줘서 안됨
    # for f in files:
    #     print(re.findall('\d{,5}', f))

    sorted1 = sorted(files, key=lambda x: int(re.findall('\d{1,5}', x)[0]))
    sorted2 = sorted(sorted1, key=lambda x: re.split('\d+', x.lower())[0])


    return sorted2
