from datetime import datetime


def format_time(datetime_obj):
    time_1 = datetime.strftime(datetime_obj,'%H:%M')
    time_2= datetime.strftime(datetime_obj,'%I:%M')
    print('24h',time_1)
    print('12h',time_2)