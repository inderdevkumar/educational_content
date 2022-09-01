#!/bin/bash

#to do: Create two function one for folder search and another for file search
#       Ask user to enter d/f  and folder name/ file name
# search in a particular folder /home/inder

echo "Enter 1 for searching a folder and 2 for searching a file"
read search_num
if [ $search_num == 1 ]; then
	echo "Enter the directory name you want to check: "
        read dir_name
        sudo find / -type d -name $dir_name
elif [ $search_num == 2 ]; then
	echo "Enter the file name you want to check: "
        read file_name
	sudo find / -type f -name $file_name
else
	echo "Please enter either 1 or 2"
fi
