#!/bin/bash


# UNfinished script. Dont use it
# WE are not able to store the output of command in varibale inside EOF/HERE. THis variable will be required in if condition to check
#

password=`cat sudopasswordfile`
host_name=`echo '$password' | sudo hostname`

sshpass -p $password ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36  << HERE
   echo "$password" | sudo -S hostname
   

host_name_normal=$(hostname)

   echo Host name:  $host_name
echo Host name:  "$host_name"
echo Host name:  \$host_name 
echo Host name: \$host_name
echo Host name: \$host_name
echo Host name: $host_name_normal

HERE


:'
host_name=`echo $HOSTNAME`
if [[ $host_name == "inder-Inspiron-14-3467" ]]; 
then 
	echo iff 
else 
	echo elsesss 
fi
'
