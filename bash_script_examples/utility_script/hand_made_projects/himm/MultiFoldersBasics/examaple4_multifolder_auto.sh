#!/usr/bin/env bash

# EDit in text file dir1/text1.txt
#sed -i 's/original/new/g' file.txt


#===============================================
echo editing text file dir1/text1.txt

echo Navigate to all folders
echo =========================================================================
echo Navigate Automatically
#for i in $(ls -d */); 
for dir in $(ls -d /home/inder/my_data/himm/MultiFoldersBasics/*/); 
do 
	#echo ${dir%%/}; 
	echo $dir
	for file in $(find $dir -type f);
	do
        	echo $file
		text_str="$(cat $file)"

		echo ========================== STart of $file ==========================================
		echo Before Editing
		echo $text_str
		arr_str=($text_str)
		str_to_check=${arr_str[2]}

		echo The word to check is: $str_to_check

		if [ $str_to_check == "Inder." ];
		then
        		echo Inside if
        		sed  -i -e "s/$str_to_check/Himadri./g" $file

		elif [ $str_to_check == "Himadri." ];
		then
        		echo Inside elif
        		sed  -i -e "s/$str_to_check/Inder./g" $file

		else
        		echo 3rd digit of string in text file should have Inder/Himadri.
		fi

		echo After Editing
		cat $file
		echo ================= End of $file ========================================================

	done
done

