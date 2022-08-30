#!/bin/bash

# URL ref: https://www.baeldung.com/linux/csv-parsing
# Another REf: https://ostechnix.com/parse-csv-files-in-bash-scripts/

# awk -F , '$6 == "India"' player_cleaned.csv


#task to do: get the sample o/p as required. eg hit_count: 30 etc.

echo
echo === Make a note, script will run with only csv file and not excel ===
echo
echo Content of csv file is
cat /home/inder/my_data/doc/task_to_do1.csv

echo
echo Filter data for hit_count >25
echo
awk 'BEGIN{FS=",";OFS=","} $6 > 25 {print $2,$3,$6}'   /home/inder/my_data/doc/task_to_do1.csv > /home/inder/my_data/doc/hit_count.csv

echo
echo Filter data for no_hit_count >25
echo
awk 'BEGIN{FS=",";OFS=","} $7 > 25 {print $2,$3,$7}'   /home/inder/my_data/doc/task_to_do1.csv > /home/inder/my_data/doc/no_hit_count.csv

echo
echo test csv to key value pair
#awk -F, 'NR==1{for(i=1;i<=NF;i++)Arr[i]=$i;next}{printf("%s,",$1);for(j=2;j<=NF;j++){printf("%s:%s,",Arr[j],$j)}printf("\n")}' /home/inder/my_data/doc/task_to_do1.csv

#awk -F, 'NR==1{for(i=1;i<=NF;i++)Arr[i]=$i;next}{printf("%s ",$1);for(j=2;j<=NF-3;j++){printf("%s: %s  ",Arr[j],$j)}printf("\n")}' /home/inder/my_data/doc/hit_count.csv


awk -F, 'NR==1{for(i=1;i<=NF;i++)Arr[i]=$i;next}{for(j=1;j<=NF;j++){printf("%s: %s  ",Arr[j],$j)}printf("\n")}' /home/inder/my_data/doc/hit_count.csv  > /home/inder/my_data/doc/all_filtered_output.txt

awk -F, 'NR==1{for(i=1;i<=NF;i++)Arr[i]=$i;next}{for(j=1;j<=NF;j++){printf("%s: %s  ",Arr[j],$j)}printf("\n")}' /home/inder/my_data/doc/no_hit_count.csv  >> /home/inder/my_data/doc/all_filtered_output.txt
