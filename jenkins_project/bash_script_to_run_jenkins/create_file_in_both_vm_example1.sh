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
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36 touch /tmp/new_file_vm1.txt
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36 ls  /tmp/
echo
echo =================================
echo
echo SSH to VM2
#ssh un pw
#ssh virtual_project@192.168.0.36 ls /tmp/
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.237 touch /tmp/new_file_vm2.txt
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.237 ls  /tmp/

echo
echo =================================
