import csv
import boto3
import datetime
import re


def fix_time(time_range):
    fixed_list = []
    new_list = time_range.replace('am', ' ').replace('to', ' ').replace('pm', ' ').replace('-', ' ').replace('p', ' ').replace('a', ' ').split()
    for i in new_list:
        if ':' in i:
            fixed_list.extend(i.split(':'))
        else:
            fixed_list.extend([i, "0"])
    return fixed_list


def set_time(time_range, time_offset):
    time_range_list = fix_time(time_range)
    date_time_list = []
    for i in range(2):
        if time_range_list[i*2] == '12':
            date_time_list.append(datetime.time(int(time_range_list[0+i*2])-1, int(time_range_list[1+i*2])))
        else:
            date_time_list.append(datetime.time(int(time_range_list[0+i*2])+time_offset-1, int(time_range_list[1 + i*2])))
    return date_time_list


def find_day(time_range, offset_left, schedule, time_offset):
    time_range_list = set_time(time_range, time_offset)
    if offset_left < schedule['Sun']['offsetLeft']:
        schedule['Sun']['times'].append(time_range_list)
    elif offset_left < schedule['Mon']['offsetLeft']:
        schedule['Mon']['times'].append(time_range_list)
    elif offset_left < schedule['Tue']['offsetLeft']:
        schedule['Tue']['times'].append(time_range_list)
    elif offset_left < schedule['Wed']['offsetLeft']:
        schedule['Wed']['times'].append(time_range_list)
    elif offset_left < schedule['Thu']['offsetLeft']:
        schedule['Thu']['times'].append(time_range_list)
    elif offset_left < schedule['Fri']['offsetLeft']:
        schedule['Fri']['times'].append(time_range_list)
    elif offset_left < schedule['Sat']['offsetLeft']:
        schedule['Sat']['times'].append(time_range_list)
    return schedule


def fill_schedule(response, schedule):
    time_offset = 0
    regex = '^([0-1]?)([0-9])(([ap]m)?|(:[0-5][0-9])?)\s*([ap]m)?(\s*to)?((\s*-\s*)|(\s+))([0-1]?)([0-9])(([ap]m)?|(:[0-5][0-9])?)\s*([ap]m)?$'
    for i in response:
        if i['Text'] in ['Sun', 'SUN', 'Sunday']:
            schedule['Sun']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Mon', 'MON', 'Monday']:
            schedule['Mon']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Tue', 'TUE', 'Tuesday']:
            schedule['Tue']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Wed', 'WED', 'Wednesday']:
            schedule['Wed']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Thu','THU','Thursday']:
            schedule['Thu']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Fri','FRI','Friday']:
            schedule['Fri']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] in ['Sat', 'SAT', 'Saturday']:
            schedule['Sat']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif re.match(regex, i['Text']) and i['BlockType'] == "LINE":
            find_day(i['Text'], i['Geometry']['BoundingBox']['Left'], schedule, time_offset)
        elif 'pm' in i['Text'] or 'PM' in i['Text']:
            time_offset = 12
    return schedule


def create_schedule(img_bytes):
    with open('accessKeys.csv', 'r') as keys:
        next(keys)
        reader = csv.reader(keys)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    client = boto3.client('textract',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)
    response = client.detect_document_text(Document={'Bytes': img_bytes})
    iresponse = iter(response['Blocks'])
    next(iresponse)
    schedule = {
        'Sun': {'offsetLeft': 0, 'times': []},
        'Mon': {'offsetLeft': 0, 'times': []},
        'Tue': {'offsetLeft': 0, 'times': []},
        'Wed': {'offsetLeft': 0, 'times': []},
        'Thu': {'offsetLeft': 0, 'times': []},
        'Fri': {'offsetLeft': 0, 'times': []},
        'Sat': {'offsetLeft': 0, 'times': []}
    }
    schedule = fill_schedule(iresponse, schedule)
    # for k in schedule:
    #     print(k, ':', schedule[k]['times'])
    return schedule

