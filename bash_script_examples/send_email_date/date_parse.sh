
#!/bin/bash

Year=`date +%Y`
Month=`date +%m`
Day=`date +%d`
Hour=`date +%H`
Minute=`date +%M`
Second=`date +%S`

echo ==========================================
echo `date`
echo Program is to split date into year, month, day, Hour,Min, Sec and than find the duration of program execution
echo
echo ==========================================
echo
echo "Current Date is: $Day-$Month-$Year"
echo "Current Time is: $Hour:$Minute:$Second"

echo waiting for 10s. Your Program code
sleep 10

echo Your Program ends here

Hour2=`date +%H`
Minute2=`date +%M`
Second2=`date +%S`
echo "Current Time is: $Hour2:$Minute2:$Second2"

#Convert all in seconds
#time1= 14:20:30
#time2= 15:05:05

(( time1=(Hour*60*60)+(Minute*60)+(Second) ))
(( time2=(Hour2*60*60)+(Minute2*60)+(Second2) ))
(( time_diff=time2-time1 ))

Hour_diff=$(bc <<< "${time_diff}/3600")
Minute_diff=$(bc <<< "(${time_diff}%3600)/60")
Second_diff=$(bc <<< "${time_diff}%60")


echo Time1 in sec $time1, Time2 in sec: $time2, Time_diff in sec: $time_diff
echo
echo Time taken to execute the program is:
printf "%02d:%02d:%02d\n" $Hour_diff $Minute_diff $Second_diff
echo

