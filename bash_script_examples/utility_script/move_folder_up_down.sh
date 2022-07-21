#!/usr/bin/env bash

echo Enter 1 to go up and 0 to down for navigatiing directory 
read up_down

echo Enter how many Ups/Down u like to navigate
read up_down_level

#for i in $up_down_level
for (( c=1; c<=$up_down_level; c++ ))
do
	if [ $up_down == 1 ];
	then
		echo Going $c step up
		pwd
		variable=$(cd ..)
		$variable
		pwd
	elif [ $up_down == 0 ];
	then
		echo  Going $c step down
	fi

done
