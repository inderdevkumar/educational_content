#!/bin/bash

#n=10

while true
do
	echo enter any number
read n
#if [ $n -lt 10 ];  #only for integer
if [[ $n < 0.5 ]];  #For decimal
then
echo "It is a one digit number"
else
echo "It is a two digit number"
fi
done
