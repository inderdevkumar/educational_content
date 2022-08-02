#!/usr/bin/env bash
echo
echo =================================
echo My first Jenkin Job
echo
echo =================================
echo Todays date time
date
echo
echo =================================
echo SSH to VM1
#ssh un pw
#ssh virtual_project@192.168.0.36 ls /tmp/
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36 touch /tmp/new_file.txt
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36 ls  /tmp/

echo SSH to VM2
#ssh un pw
#ssh virtual_project@192.168.0.36 ls /tmp/
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.237 touch /tmp/new_file.txt
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.237 ls  /tmp/

echo
echo =================================
echo Creating A new File in this system
touch /tmp/new_file.txt
echo
echo =================================
echo check FRom when the system is on
uptime
echo
echo =================================
echo IP of system and User name
ifconfig | grep "inet 19" | awk  '{print $2}'

echo Username is: `whoami`
echo
echo =================================


