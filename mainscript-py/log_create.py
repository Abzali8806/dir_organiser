import datetime
import csv
from os import write


def addtolog(filename, path):
    cwt = datetime.datetime.now()
    with open('/home/abz/Desktop/dir_organiser0.2/logs.csv', mode='a') as f:
        f_writer = csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_writer.writerow([filename, path, cwt.time()])

