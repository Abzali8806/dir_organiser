import os
import shutil
from log_create import csv_func

from os import walk

#condition variables
source = '/path/to/Downloads/'



def directories_content():
    d_f = [] # download files
    for (dirpath, dirnames, filenames) in walk('/path/to/Downloads/'): # get's files in downloads directory
        d_f.extend(filenames) # put's filesnames into d_f list
        break # breaks after first iteration - hence only filenames in initial Downloads directory are retrieved 
            # instead of sub-directories.

    r_f = [] # resume directory
    for (dirpath, dirnames, filenames) in walk('/path/to/CV_folder/'):
        r_f.extend(filenames)
        break

    iso_f = [] # iso fie directory
    for (dirpath, dirnames, filenames) in walk('/path/to/iso_folder'):
        r_f.extend(filenames)
        print(filenames)
        break
    return d_f, r_f, iso_f

dir_content = directories_content()

d_f = dir_content[0]
r_f = dir_content[1]
iso_f = dir_content[2]

file_type = ["cv", "cover", ".jpg", ".jpeg", ".png", ".iso"]

def des_path(type): # gets destination path of files
    resume = "cv"
    cover = "cover"
    ismatch = False

    if type.lower() == resume:
        # ismatch = True
        destination = '/path/to/CV_folder/'
    elif type.lower() == cover:
        # ismatch = True
        destination = '/path/to/CV/cover_folders/'
    elif type.lower() == ".jpg" or type.lower() == ".jpeg" or type.lower() == ".png":
        # ismatch = True
        destination = '//path/to/Pictures/'
    elif type.lower() == ".iso":
        # ismatch = True
        destination = '/path/to/iso_folder/'
    else:
        # ismatch = False
        pass
    
    return destination


for file in d_f:
    for type in file_type:
        if type.lower() in file.lower():
            ismatch = True
            d_path = des_path(type)
            if file in r_f:
                os.remove(source+file)
            elif file in iso_f:
                os.remove(source+file, d_path)
                print('file deleted')
            else:
                shutil.move(source+file, d_path)
                csv_func(file, d_path)
        else:
            pass