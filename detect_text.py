import csv
import boto3
import datetime


def set_time(time_range, time_offset):
    time_range_list = time_range.replace('-', ' ').replace(':', ' ').replace('p', ' ').split()
    date_time_list = [datetime.time(int(time_range_list[0])+time_offset-1, int(time_range_list[1])),
                      datetime.time(int(time_range_list[2])+time_offset-1, int(time_range_list[3]))]
    return date_time_list


def find_day(time_range, offset_left, schedule, time_offset):
    time_range_list = set_time(time_range, time_offset)
    if offset_left < schedule['Mon']['offsetLeft']:
        schedule['Mon']['times'].append(time_range_list)
    elif offset_left < schedule['Tue']['offsetLeft']:
        schedule['Tue']['times'].append(time_range_list)
    elif offset_left < schedule['Wed']['offsetLeft']:
        schedule['Wed']['times'].append(time_range_list)
    elif offset_left < schedule['Thu']['offsetLeft']:
        schedule['Thu']['times'].append(time_range_list)
    elif offset_left < schedule['Fri']['offsetLeft']:
        schedule['Fri']['times'].append(time_range_list)
    return schedule


def fill_schedule(response, schedule):
    time_offset = 0
    for i in response:
        if i['Text'] == 'Mon':
            schedule['Mon']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] == 'Tue':
            schedule['Tue']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] == 'Wed':
            schedule['Wed']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] == 'Thu':
            schedule['Thu']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif i['Text'] == 'Fri':
            schedule['Fri']['offsetLeft'] = i['Geometry']['BoundingBox']['Left']
        elif ':' in i['Text'] and i['BlockType'] == "LINE":
            find_day(i['Text'], i['Geometry']['BoundingBox']['Left'], schedule, time_offset)
        elif 'pm' in i['Text']:
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
    client1 = boto3.client('rekognition',
                           aws_access_key_id=access_key_id,
                           aws_secret_access_key=secret_access_key)

    response = client.detect_document_text(Document={'Bytes': img_bytes})
    iresponse = iter(response['Blocks'])
    next(iresponse)
    schedule = {
        'Mon': {'offsetLeft': 0, 'times': []},
        'Tue': {'offsetLeft': 0, 'times': []},
        'Wed': {'offsetLeft': 0, 'times': []},
        'Thu': {'offsetLeft': 0, 'times': []},
        'Fri': {'offsetLeft': 0, 'times': []},
    }
    schedule = fill_schedule(iresponse, schedule)
    return schedule


# with open('schedule.png', 'rb') as source_image:
#     source_bytes = source_image.read()
# create_schedule(source_bytes)
