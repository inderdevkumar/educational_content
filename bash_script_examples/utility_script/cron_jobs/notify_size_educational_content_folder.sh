#!/bin/bash
echo `date`


	echo ========================================================================
	echo Size of /home/inder/my_data/educational_content to Aavaoid problem in pushing to git
	echo It should be less than 80MB
	echo ========================================================================
	echo
	
	Red=$'\e[1;31m'
	Green=$'\e[1;32m'
	Yellow=$'\e[1;33m'
	Blue=$'\e[1;34m'
	White=$'\e[1;37m'

	cd /home/inder/my_data/educational_content	
	all_files_folders=`du -sh $(ls -A)`

	echo mem in folder is just a list of files/folder with size. seperate the files and size and check the condition with size
	echo convert the size in mbs. Convert both kb/gb to mb

	array1_size=($(du -sh $(ls -A) | awk '{ print $1 }'))
	array2_file_folder_names=($(du -sh $(ls -A) | awk '{ print $2 }'))

	echo  "memory available in Folder:  $all_files_folders"
	echo ========================================================================
	echo
	#echo  "memory available in Folder:  $array1_size"
	#echo  "Length of array1 is:  ${#array1_size[@]}"
	#echo  2nd position of array1 is: " ${array1_size[2]}"
	#echo  "Length of array2 is:  ${#array2_file_folder_names[@]}"
        #echo  2nd position of array2 is: " ${array2_file_folder_names[2]}"


# CHeck and modify array1
       array1_all_modified=()

        for item in "${array1_size[@]}"
	do
		
		if [[ $item == *K* ]]
		then
			#Remove the last charcater
			remove_last_char=${item::-1}
			
			if [[ $remove_last_char == *,* ]]
			then
		
				#REplace comma with .
				#remove_comma_n_last_char=`"$remove_last_char" | tr "," .`
				remove_comma_n_last_char=${remove_last_char//[,]/.}
				
				kb_to_mb=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]/ARGV[2]}' "$remove_comma_n_last_char" "1024"`
				array1_all_modified+=($kb_to_mb)
				
			else
				kb_to_mb=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]/ARGV[2]}' "$remove_last_char" "1024"`				
				array1_all_modified+=($kb_to_mb)
				
			fi
			
			
		elif [[ $item == *G* ]]
		then 

			#Remove the last charcater
			remove_last_char=${item::-1}
			if [[ $remove_last_char == *,* ]]
			then

		
		              #REplace comma with .
			      #remove_comma_n_last_char=`"$remove_last_char" | tr "," .`
			      remove_comma_n_last_char=${remove_last_char//[,]/.}

			      gb_to_mb=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]*ARGV[2]}' "$remove_comma_n_last_char" "1024"`
			      array1_all_modified+=($gb_to_mb)

		      else
			       gb_to_mb=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]*ARGV[2]}' "$remove_last_char" "1024"`
			       
			       array1_all_modified+=($gb_to_mb) 
		      fi

        	else

                        
                        #Remove the last charcater
                        remove_last_char=${item::-1}
                        if [[ $remove_last_char == *,* ]]
			then 
		
				remove_comma_n_last_char=${remove_last_char//[,]/.}
                                size_in_mb=`$remove_comma_n_last_char`
			else
			     
			        size_in_mb=`$remove_comma_n_last_char`
			
				array1_all_modified+=($size_in_mb)
			fi

		fi
	done
	

	#for value in "${array1_all_modified[@]}"
	for (( i=0; i<=$(( ${#array1_size[@]} -1 )); i++ ))
	
	do	
		
		
		if [[ "${array1_all_modified[i]%%.*}" -ge 80 ]];
		then
			echo ========================================================================
        		echo
    			echo "$Red Delete Unwanted files"
			echo Files/Folder name is: ${array2_file_folder_names[i]}
                	echo Size is: ${array1_size[i]}
			echo $White

		elif [[ "${array1_all_modified[i]%%.*}" -lt 80 && "${array1_all_modified[i]%%.*}" -ge 50 ]];
		then 
			
    			echo ========================================================================
        		echo
			echo "$Yellow Warning !!!"	
			echo Files/Folder name is: ${array2_file_folder_names[i]}
                	echo Size is: ${array1_size[i]}
			echo $White

		else	
			
 			echo ========================================================================
        		echo
			echo "$Green No Action Required"
			echo Files/Folder name is: ${array2_file_folder_names[i]}
                	echo Size is: ${array1_size[i]}
			echo $White

		fi
		
	done
echo ========================================================================
echo
echo Done
echo ========================================================================
echo
