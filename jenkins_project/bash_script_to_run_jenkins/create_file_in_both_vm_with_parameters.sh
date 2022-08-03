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

#all_vms_ip=(192.168.0.36 192.168.0.237)


all_vms_ip_array=(`echo $all_vms_ip | tr ',' ' '`)

for item in "${all_vms_ip_array[@]}"
do
	
	echo ==============
	echo SSH to $item
	echo ==============

	echo create file, list craetd file, uptime, hostname, df -h
	sshpass -p "kumar0102" ssh -o StrictHostKeyChecking=no virtual_project@$item << EOF
	touch /tmp/new_file_vm1.txt
	ls  /tmp/
	
EOF
done

echo
echo ===============  END ==================
