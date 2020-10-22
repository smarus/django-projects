from datetime import datetime


def get_release_date(release_str):
    c = release_str.split()
    date_str = '/'.join(c[-3:])
    return datetime.strptime(date_str, "%d/%B/%Y")