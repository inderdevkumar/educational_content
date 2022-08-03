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

echo create file, list craetd file, uptime, hostname, df -h

sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36 << EOF
touch /tmp/new_file_vm1.txt
ls  /tmp/
EOF
echo
echo =================================
echo
echo SSH to VM2
echo create file, list craetd file, uptime, hostname, df -h
#ssh un pw
#ssh virtual_project@192.168.0.36 ls /tmp/
sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.237 << EOF
touch /tmp/new_file_vm2.txt
ls  /tmp/
EOF
echo
echo =================================
