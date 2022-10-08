#!/bin/bash
Year=`date +%Y`
Month=`date +%m`
Day=`date +%d`
Hour=`date +%H`
Minute=`date +%M`
Second=`date +%S`

echo `date`
echo "Current Date is: $Day-$Month-$Year"
echo "Current Time is: $Hour:$Minute:$Second"

echo waiting for 10s
sleep 10
Hour2=`date +%H`
Minute2=`date +%M`
Second2=`date +%S`
echo "Current Time is: $Hour2:$Minute2:$Second2"
echo "Current Time is: $Hour:$Minute:$Second"
Hour_dff= 1

echo Time Difference is: 
