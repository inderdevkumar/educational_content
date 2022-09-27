#!/bin/bash
echo content of text file is
cat /home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/filter_data_from_text_file/all_data.txt
echo filter data with a date range
echo
#To get all columns
echo 
echo To get all columns

awk '$3 >= "25-09-2022" && $3 <= "27-09-2022" { print $0 }' all_data.txt
#To get specific columns
echo 
echo To get specific columns

awk '$3 >= "25-09-2022" && $3 <= "27-09-2022" { print $1" "$3 }' all_data.txt > bash_filter_output.txt
