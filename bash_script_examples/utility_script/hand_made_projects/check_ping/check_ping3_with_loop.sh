#!/usr/bin/env bash

Red=$'\e[1;31m'
Green=$'\e[1;32m'
Blue=$'\e[1;34m'
White=$'\e[1;37m'
myArray=("192.124.0.191" "192.124.0.192" "192.124.0.193" "192.124.0.190")

for TARGET in ${myArray[@]}; 
do
  
  echo $White Checking ping for $TARGET
  DATE=$(date '+%d/%m/%Y %H:%M:%S')
  ping -c 1 $TARGET &> /dev/null

            #ping -c 1 $TARGET
  if [[ $? -ne 0 ]];   #$?-The exit status of the last command executed.
  then
       echo "$Red Failure in date: "$DATE
       echo "Failure in date: "$DATE >> $FILE
  else
       echo "$Green Success in date: "$DATE
  fi

  sleep 5

done



