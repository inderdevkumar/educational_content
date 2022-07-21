#!/usr/bin/env bash

Red=$'\e[1;31m'
Green=$'\e[1;32m'
Blue=$'\e[1;34m'
White=$'\e[1;37m'
myArray=("192.124.0.191" "192.124.0.192" "192.124.0.193" "192.124.0.190")
count=0
for TARGET in ${myArray[@]}; 
do
  

  echo $White Checking ping for $TARGET
  DATE=$(date '+%d/%m/%Y %H:%M:%S')
  ping -c 1 $TARGET &> /dev/null
            
  if [[ $? -ne 0 ]];   #$?-The exit status of the last command executed.
  then
       echo "$Red Failure in date: "$DATE
       while [ $count -lt 3 ];
       do
	       echo Re trying $count times for $TARGET
	       ping -c 1 $TARGET &> /dev/null
	       if [[ $? -ne 0 ]];   #$?-The exit status of the last command executed.
  	       then
                   echo "$Red Failure in date: "$DATE
		   count=$(($count + 1))
	       else
                   echo "$Green Success in date: "$DATE
                   count=4
               fi
               
	       echo Sleep for 2s
	       sleep 2
        done
              
  else
       echo "$Green Success in date: "$DATE       
  fi
  echo Sleep for 2s
  sleep 2
  count=0

done



