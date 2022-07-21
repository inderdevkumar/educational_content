#!/usr/bin/env bash

TARGET="$(ifconfig | grep '192' | awk '{print $2}')"
echo IP of your machine is:  $TARGET 
#TARGET=192.124.0.190

FILE=ping_error.txt

Red=$'\e[1;31m'
Green=$'\e[1;32m'
Blue=$'\e[1;34m'

touch $FILE
while true;
do
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
