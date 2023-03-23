

"""
Problem statement:
I have a few folders. In each folder, there is a text file that has information.
 This file's name in each folder needs to be modified.
 My folder name is INQ_AWS8976 etc we need to pull AWS8976 and assign this folder name to the file in it

"""

import os

# folder path
dir_path = "/home/inder/my_data/upwork_data/march_2023/23_march"

# list to store files
all_dir = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        pass

    else:
        new_path= dir_path+ "/"+ path
        for files in os.listdir(new_path):
            old_file_path= os.path.join(new_path, files)

            new_name= path[4:]+".txt"

            new_file_path= os.path.join(new_path, new_name)

            os.rename(old_file_path, new_file_path)
        all_dir.append(path)
print(all_dir)



