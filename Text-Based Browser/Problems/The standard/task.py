from datetime import datetime


def convert_to_standard(datetime_obj):
    day = datetime.strftime(datetime_obj, '%Y-%m-%d')
    return day