import os
import shutil
from log_create import csv_func

from os import walk

#condition variables
resumes = "CV"
Covers = "Cover"
source = '/home/abz/Downloads'




d_f = [] # download files
for (dirpath, dirnames, filenames) in walk('/home/abz/Downloads'): # get's files in downloads directory
    d_f.extend(filenames) # put's filesnames into d_f list
    break # breaks after first iteration - hence only filenames in initial Downloads directory are retrieved 
          # instead of sub-directories.

r_f = [] # resume directory
for (dirpath, dirnames, filenames) in walk('/home/abz/resume'):
    r_f.extend(filenames)
    break

iso_f = [] # iso fie directory
for (dirpath, dirnames, filenames) in walk('/home/abz/iso_folder'):
    r_f.extend(filenames)
    print(filenames)
    break

def des_path(file): # gets destination path of files
    global resumes
    global Covers
    if resumes.lower() in file:
        destination = '/home/abz/CV/'
    elif Covers.lower() in file:
        destination = '/home/abz/CV/covers'
    elif ".jpg".lower() in file or ".jpeg".lower() in file or "png".lower() in file:
        destination = '/home/abz/Images/'
    elif ".iso".lower() in file:
        destination = '/home/abz/iso_folder/'
    return destination

loop_count = 0
for file in d_f:
    d_path = des_path(file)
    print(file)
    if file in r_f:
        os.remove(source+file)
    elif "CV".lower() in file.lower():
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
    elif "Cover".lower() in file.lower():
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
    elif file in iso_f:
        os.remove(source+file, d_path)
        print('file deleted')
    elif '.iso' in file:
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
    elif '.jpg'.lower() in file.lower():
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
    elif '.jpeg'.lower() in file.lower():
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
    elif '.png'.lower() in file.lower():
        shutil.move(source+file, d_path)
        csv_func(file, d_path)
        loop_count+=1
