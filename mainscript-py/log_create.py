import datetime
import csv
from os import write


def csv_func(filename, path):
    with open('/home/abz/Desktop/dir_organiser/logs.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        rows_count = len(data)
    if rows_count == 0:
        with open('/home/abz/Desktop/dir_organiser/logs.csv', mode='w') as f:
            f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f_writer.writerow([" Filename", " Path", " Date", " Time"])
    else:
        cwt = datetime.datetime.now()
        with open('/home/abz/Desktop/dir_organiser/logs.csv', mode='a') as f:
            f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f_writer.writerow([f"{filename}, {path}, {cwt.date()}, {cwt.time()}"])


def log_heading(): 
    # cwt = datetime.datetime.now()
    with open('/home/abz/Desktop/dir_organiser/logs.csv', mode='w') as f:
        f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_writer.writerow(["Filename", "Path", "Date", "Time"])


def add2logs(filename, path):
    cwt = datetime.datetime.now()
    with open('/home/abz/Desktop/dir_organiser/logs.csv', mode='a') as f:
        f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_writer.writerow([f"{filename}, {path}, {cwt.date()}, {cwt.time()}"])
