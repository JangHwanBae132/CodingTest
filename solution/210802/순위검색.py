import re
hashMap = {};

def solution(info, query):
    allCaseHashMap(info)
    hashMapSort(hashMap)
    answer = []
    answer = MakeAnswer(query, answer);
    print(answer)
    return answer

def allCaseHashMap(info):
    # string, score[]
    for s in info:
        score = int(re.sub(r'[^0-9]', '', s))

        string = re.sub(r'[0-9]', '', s)
        split = string.split(" ")
        dfs(split, 0 , "", score)

def dfs(split, depth, string, score):
    if depth == 4:
        if string not in hashMap:
            hashMap[string] = [score]
        else:
            hashMap[string] += [score]
    else:
        dfs(split, depth+1, string+split[depth], score)
        dfs(split, depth+1, string+"-", score)

def hashMapSort(hashmap):
    for key in hashmap.keys():
        hashmap[key].sort()

def MakeAnswer(query, answer):
    for q in query:
        Qscore = int(re.sub(r'[^0-9]', '', q))
        Qstring = re.sub(r'[0-9]', '', q).replace(" and ", "").strip()
        if Qstring in hashMap:
            start =0
            end = len(hashMap[Qstring])-1
            while (start <= end):
                mid = int((start+end)/2)
                if hashMap[Qstring][mid] < Qscore:
                    start = mid+1
                else:
                    end = mid-1
            answer += [len(hashMap[Qstring]) -start];
        else:
            answer +=[0]
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["- and backend and senior and - 1500"]

# allCaseHashMap(info)

# hashMap = {'s': [6, 4], 'a': [2, 6], 'c': [3, 3, 2] }
# hashMapSort(hashMap)

solution(info, query)
