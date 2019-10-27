import datetime


def available_schedule(schedule, start, end):
    diction = {
        'Sun': {'times': []},
        'Mon': {'times': []},
        'Tue': {'times': []},
        'Wed': {'times': []},
        'Thu': {'times': []},
        'Fri': {'times': []},
        'Sat': {'times': []}
    }

    current = datetime.time(start, 0)
    last = datetime.time(end, 0)
    for i in schedule:
        for time in schedule[i]['times']:
            if int(time[0].hour) * 60 + int(time[0].minute) - int(current.hour) * 60 + int(current.minute) > 30:
                diction[i]['times'].append([current, datetime.time(time[0].hour, time[0].minute)])
                current = time[1]
            else:
                current = time[1]
        if int(last.hour) * 60 + int(last.minute) - int(current.hour) * 60 + int(current.minute) > 30:
            diction[i]['times'].append([current, last])
        current = datetime.time(start, 0)

    for j in diction:
        print(j, ':', diction[j])

    return diction
