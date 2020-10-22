from datetime import datetime


def get_weekday(datetime_obj):
    day = datetime.strftime(datetime_obj, '%A')
    return day

