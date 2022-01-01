import sys
import csv
import pyperclip

# filename input
filename = sys.argv[1] # filename you enter when running program

def cvs_entries2_datelist(filename):
    with open('/home/abz/Desktop/dir_organiser/logs.csv') as csv_file:
        
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        rows_count = len(data)
        # csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0
        entries_list = []
        date_list = []
        for row in reader:
            if filename in row[0]:
                csv_item = row[0] # each row is one conjoined item
                items_seperated = csv_item.split(", ") # item split into seperate items
                entries_list.append(items_seperated) # nested arrays of entries. passed to file_locate function
                date_list.append(items_seperated[2]) # dates of entrie of filename used
                                                     # - to retrieve latest log entry of filename
    return date_list, line_count, entries_list


result = cvs_entries2_datelist(filename)
date = result[0]
line_count= result[1]
row_entries = result[2]


def copy2clipboard(path, file):
    print("\nWould you like to copy path to clipboard?")
    query = input("y/n: ")
    if query == "y":
        pyperclip.copy(f"{path}")
    else:
        pass


def file_locate(entries, date):
    for e in entries:    
        if date == e[2]: # date comparison - cond True = latest entry of file 
            print(f"file location: {e[1]}{e[0]}") # print path
            copy2clipboard(e[1], e[0]) # copy path to clipboard
            break
        else:
            pass


date.sort() # important - sorts dates from oldest to latest
try:
    if line_count > 1:
        latest_date = date[-1]
        file_locate(row_entries, latest_date)
    else:
        latest_date = date[0]
        file_locate(row_entries, latest_date)
except IndexError:
    print("Error!\nno records in log file")


