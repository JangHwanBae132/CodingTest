from collections import deque


def solution(n, t, m, timetable):
    answer = ''
    new_timetable = []
    bus_time = [540 + i*t for i in range(n)]

    for t in  timetable:
        split_t = t.split(":")
        new_timetable.append(int(split_t[0])*60+int(split_t[1]))

    new_timetable.sort()

    queue = deque(new_timetable)

    for bus in bus_time:
        passenger = []

        while len(queue) != 0 and queue[0]<= bus and len(passenger) < m:
            passenger.append(queue.popleft())
        if len(passenger) == m:
            if passenger[0] == passenger[m-1]:
                answer = passenger[0]-1
            else:
                answer = passenger[m-1]-1
        else:
            answer = bus

    str_ans = ""
    if len(str(int(answer/60))) == 2:
        str_ans += str(int(answer/60))
    else:
        str_ans += "0"+str(int(answer / 60))

    if len(str(answer % 60)) == 2:
        str_ans += ":"+str(answer % 60)
    else:
        str_ans += ":0" + str(answer % 60)

    return str_ans
