import os
import shutil

from os import walk


path = '/home/abdullah/Downloads'
destination = '/home/abdullah/resume'


d_f = [] # empty list - stands for download files
for (dirpath, dirnames, filenames) in walk('/home/abdullah/Downloads'): # get's files in downloads directory
    d_f.extend(filenames) # put's filesnames into d_f list
    break # breaks after first iteration - hence only filenames in initial Downloads directory are retrieved 
          # instead of sub-directories.


# resume directory
r_f = []
for (dirpath, dirnames, filenames) in walk('/home/abdullah/resume'):
    r_f.extend(filenames)
    break

# iso fie directory
iso_f = []
for (dirpath, dirnames, filenames) in walk('/home/abdullah/iso_folder'):
    r_f.extend(filenames)
    break

for i in d_f:
    # C.V files
    if i in r_f:
        os.remove("/home/abdullah/Downloads/"+i)
    elif 'CV' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/resume/')
    elif 'Cover' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/resume/')
    # iso files
    elif i in iso_f:
        os.remove("/home/abdullah/Downloads/"+i)
        print('file deleted')
    elif '.iso' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/iso_folder/')
        print('file moved')
    # Image files
    elif 'jpg' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/Images/')
    elif 'jpeg' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/Images/')
    elif 'png' in i:
        shutil.move('/home/abdullah/Downloads/'+i, '/home/abdullah/Images/')