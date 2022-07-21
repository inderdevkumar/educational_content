#!/usr/bin/env bash

# EDit in text file dir1/text1.txt
#sed -i 's/original/new/g' file.txt


#===============================================
echo editing text file dir1/text1.txt

echo Navigate to all folders
echo =========================================================================
echo Navigate Manually
echo ================= dir1 ========================================================
cd /home/inder/my_data/himm/MultiFoldersBasics/dir1
echo LIsting all files under /home/inder/my_data/himm/MultiFoldersBasics/dir1
ls
echo ================= dir2 ========================================================
cd /home/inder/my_data/himm/MultiFoldersBasics/dir2
echo LIsting all files under /home/inder/my_data/himm/MultiFoldersBasics/dir2
ls
echo ================= dir3 ========================================================
cd /home/inder/my_data/himm/MultiFoldersBasics/dir3
echo LIsting all files under /home/inder/my_data/himm/MultiFoldersBasics/dir3
ls
echo ================= dir4 ========================================================
cd /home/inder/my_data/himm/MultiFoldersBasics/dir4
echo LIsting all files under /home/inder/my_data/himm/MultiFoldersBasics/dir4
ls
echo =========================================================================



: '
text_str="$(cat /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt)"

echo Before Editing
echo $text_str
arr_str=($text_str)
str_to_check=${arr_str[2]}

echo The word to check is: $str_to_check  "$str_to_check"

if [ $str_to_check == "Inder." ];
then
	echo Inside if 
	sed  -i -e "s/$str_to_check/Himadri./g" /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt

elif [ $str_to_check == "Himadri." ];
then
	echo Inside elif 
	sed  -i -e "s/$str_to_check/Inder./g" /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt

else
	echo 3rd digit of string in text file should have Inder/Himadri.
fi

echo After Editing
cat /home/inder/my_data/himm/MultiFoldersBasics/dir1/text1.txt
'
