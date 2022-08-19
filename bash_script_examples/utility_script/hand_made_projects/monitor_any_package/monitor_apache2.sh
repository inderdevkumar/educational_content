#!/usr/bin/env bash
all_vms_ip=(192.168.0.36 192.168.0.237)

for item in "${all_vms_ip[@]}"
do
	
	echo ==============
	echo SSH to $item
	echo ==============
	password=`cat sudopasswordfile`
	sshpass -p  $password ssh -o StrictHostKeyChecking=no virtual_project@$item << EOF
	
	echo Check if Apache2 is installed or not
	
	cat /etc/apache2/apache2.conf > /dev/null
	if [[ $? -eq 0 ]]; then
		echo Apache2 is already installled
	 	
        else
		echo "Apache2 tool need to be installed"
                sudo apt-get install apache2
		
	fi
	
	echo CHecking for Apache2 service running or not

	apache2_status=$(sudo -S systemctl status apache2)
	apache2_stop=$(sudo systemctl stop apache2)
	apache2_start=$(sudo systemctl start apache2)

	
	if [[ \$apache2_status == *"active (running)"* ]]; then
		echo "process is running"
		else echo "process is not running"
	
	elif [[ echo \$apache2_status == *"inactive (dead)"* ]]; then
		echo Apache2 is not running
		echo STarting Apache2
		\$apache2_start
		
	fi

EOF
done



