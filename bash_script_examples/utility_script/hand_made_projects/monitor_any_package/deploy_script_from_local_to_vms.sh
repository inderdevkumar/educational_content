#/bin/bash


# UNfinished script. Dont use it
# WE are not able to store the output of command in varibale inside EOF/HERE. THis variable will be required in if condition to check
#

all_vms_ip=(192.168.0.36 192.168.0.237)
password=`cat sudopasswordfile`

for item in "${all_vms_ip[@]}"
do
	echo ========================================
	echo
	echo $item
	# Copy Script file from local to VMs
	echo Copy Script file from local to VMs
	sshpass -p $password scp monitor_apache_copy_and_run_in_vm.sh virtual_project@$item:/tmp

	# TO run SCript in VMs
	echo TO run SCript in VMs
	sshpass -p $password ssh -o StrictHostKeyChecking=no virtual_project@$item "sh /tmp/monitor_apache_copy_and_run_in_vm.sh"
	echo
	echo ========================================
done
