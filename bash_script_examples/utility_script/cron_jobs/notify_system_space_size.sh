#!/bin/bash
echo `date`

mem_usage () {

Red=$'\e[1;31m'
Green=$'\e[1;32m'
Yellow=$'\e[1;33m'
Blue=$'\e[1;34m'
White=$'\e[1;37m'
 #MB units
	mem_free=`df -h | grep "/dev/sda2" | awk '{print $4+$6}'`
	RAM_KB=$(grep MemTotal /proc/meminfo | awk '{print $2}')
	(( to_divide=1024*1024 ))
        #Dell Inspiron-14-3467 intel processor  --- need to print
	Product_Name=`cat /sys/class/dmi/id/product_name`
	manufacture_Name=`cat /sys/class/dmi/id/chassis_vendor`
	Processor_Name=`awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ \t]*//'`
	
	ram_in_gb_with_decimal=`awk -- 'BEGIN{printf "%.3f\n", ARGV[1]/ARGV[2]}' "$RAM_KB" "$to_divide"`

	cd /home/inder/my_data/educational_content	
	mem_in_folder=`du -sh $(ls -A)`


	echo "memory Available is : $mem_free GB"



	
	if [ $mem_free -le 200  ]
	then
    		echo "$Red Delete Unwanted files"
                echo "$White" 
	elif [[ $mem_free -gt 200 && $mem_free -le 400 ]]
	then 
    		echo "$Yellow Warning !!!"	
                echo "$White"

	elif [ $mem_free -gt 400 ]
	then 
 		 echo "$Green No Action Required"	
		 echo "$White"

	else
    		echo "$Blue No Condition is satisfied "
		echo "$White"
	fi


	echo "RAM available is : $ram_in_gb_with_decimal GB"
        #str=`$manufacture_Name  $Product_Name  $Processor_Name`
	echo $manufacture_Name  $Product_Name  $Processor_Name | awk '{ print $1" "$3 $4" " $5" "$7}'

}

mem_usage
