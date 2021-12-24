import os
import shutil
from log_create import addtolog

from os import walk

#condition variables
resumes = "CV"
Covers = "Cover"

path = '/home/abz/Downloads'
destination = '/home/abz/resume'


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
    break

for file in d_f:
    # C.V files
    if file in r_f:
        os.remove("/home/abz/Downloads/"+file)
    elif resumes.lower() in file.lower():
        shutil.move('/home/abz/Downloads/'+file, '/home/abz/resume/')
        addtolog(file, '/home/abz/resume/')
    elif Covers.lower() in file.lower():
        shutil.move('/home/abz/Downloads/'+file, '/home/abz/resume/covers')
        addtolog(file, '/home/abz/resume/covers')
    else:    
        if file in iso_f:
            os.remove("/home/abz/Downloads/"+file)
            print('file deleted')
        elif '.iso' in file:
            shutil.move('/home/abz/Downloads/'+file, '/home/abz/iso_folder/')
            addtolog(file, '/home/abz/iso_folder/')
        else:
            # Image files
            if '.jpg'.lower() in file.lower():
                shutil.move('/home/abz/Downloads/'+file, '/home/abz/Images/')
                addtolog(file, '/home/abz/Images/')
            elif '.jpeg'.lower() in file.lower():
                shutil.move('/home/abz/Downloads/'+file, '/home/abz/Images/')
                addtolog(file, '/home/abz/Images/')
            elif '.png'.lower() in file.lower():
                shutil.move('/home/abz/Downloads/'+file, '/home/abz/Images/')
                addtolog(file, '/home/abz/Images/')
