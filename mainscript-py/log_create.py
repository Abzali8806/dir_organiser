import datetime
import csv
from os import write


def csv_func(filename, path):
    with open('/path/to/logs.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        rows_count = len(data)
        # print(data)
        # print(rows_count)
    if rows_count == 0:
        with open('/path/to/logs.csv', mode='w') as f:
            f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f_writer.writerow([" Filename", " Path", " Date", " Time"])
    else:
        cwt = datetime.datetime.now()
        with open('/path/to/logs.csv', mode='a') as f:
            f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f_writer.writerow([f"{filename}, {path}, {cwt.date()}, {cwt.time()}"])

