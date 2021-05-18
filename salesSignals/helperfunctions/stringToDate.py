import datetime


def stringToDate(row):

    if isinstance(row, str) is True:
        row = datetime.datetime.strptime(row, '%Y-%m-%d')
    return row
