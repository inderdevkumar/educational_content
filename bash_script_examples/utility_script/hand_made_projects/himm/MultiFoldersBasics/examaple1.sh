#!/usr/bin/env bash

# EDit in text file dir1/text1.txt
#sed -i 's/original/new/g' file.txt

echo Listing all files
ls -al


echo editing text file dir1/text1.txt
cat /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt
sed  -i -e 's/Inder/laudu/g' /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt
echo After Editing
cat /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt

