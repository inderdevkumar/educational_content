#!/usr/bin/env bash

#========== WE can do from 3 approaches
#1. FRom bash-> Using EOF-> Does not work
#               Using Copy Paste-> Means, create a script that can be run in standalone machine than working script shoould be copied 
#                                  to VMs /tmp folder and there just execute the script. After completion just remove the script 
#                                  from both VMs /tmp folder
#2. From ansible
#3. From Jenkins
#=====================

#=====================

#===

	
	echo Check if Apache2 is installed or not. It will just read the apache2 file	

	cat /etc/apache2/apache2.conf > /dev/null
	echo $?
	if [ $? -eq 0 ]; then
		echo Apache2 is already installled
	 	
        else
		echo "Apache2 tool need to be installed"
		#HOw to automate for yes or no prmopt ehile installing
		#===
                echo "kumar0102" | sudo -S apt-get install -y apache2
		
	fi
	
	echo CHecking for Apache2 service running or not
	#check_apache_service_available_or_not=`service --status-all | grep "cron" | awk '{print $4}'`
	apache2_status=`echo "kumar0102" | sudo -S systemctl status apache2`
	#apache2_status=`echo "kumar0102" | sudo -S service ssh status`
	apache2_stop=`echo "kumar0102" | sudo systemctl stop apache2`
	apache2_start=`echo "kumar0102" | sudo systemctl start apache2`
        
	echo ==========Apache2 status  ====
	echo
	
	echo
	echo =================
	
	if [[ "$apache2_status" == *"active (running)"* ]]; then
		echo "process is running"
		echo CHeck the Apache2 Process id
		#===https://www.cyberciti.biz/faq/bash-check-if-process-is-running-or-notonlinuxunix/
		pidof -x apache2
		
	
	elif [[ "$apache2_status" == *"inactive (dead)"* ]]; then
		echo Apache2 is not running
		echo STarting Apache2
		$apache2_start
		echo CHeck the Apache2 Process id
		#===
		pidof -x apache2


	else 
		 echo ================================
		 echo "Look like something wrong with Apache2. Check and RE-test"
		 echo ================================
	fi



