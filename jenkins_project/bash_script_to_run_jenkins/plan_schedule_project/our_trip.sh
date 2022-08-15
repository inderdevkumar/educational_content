#!/bin/bash

array_of_jouney=("mum_to_hyd" "hyd_to_ranchi_flight" "ranchi_to_kqr_bus/train" "bbs_to_kqr" "kqr_to_bbs" "hyd_to_bbs" "bbs_to_kqr" "kqr_to_bbs" "kqr_to_puri" "puri_to_njp" "njp_to_hwh" "hwh_to_hyd" "hyd_to_mum")

array_of_jouney_people=("Inder" "Inder" "Inder" "parents" "parents" "Himadri" "Parents" "Parents" "Inder_Himadri" "Inder_Himadri" "Inder_Himadri" "Inder")

array_train_name=("Vishakha Express" "Purushottam Express" "Nandankanan Express" "Purushottam Express" "Ghy SC Express" "Saraighat Express" "SC Express" "7" "8" "9" "10" "11" "12") 

array_train_no=("1" "12" "123" "1234" "12345" "123456" "1234567" "12345678" "123456789" "1234567890" "1se11" "1se12")
array_seat_no=("ac3_1" "ac3_1_2" "ac3_1" "sl_1_2_3_4_5_6" "sl_11_12_13_14_15_16"  "sl_1_2_3_4_5_6" "sl_11_12_13_14_15_16" "ac3_2_3" "ac3_4_5" "ac3_6_7" "ac3_8_9" "ac3_1_3" "ac3_1")

array_of_time=("14:00-03:20" "17:35-19:20" "21:05-01:23" "23:05-12:01" "22:50-11:40" "16:50-15:25" "12:30-04:16" "14:01-03:30" "14:01-05:25" "22:05-18:45" "16:25-06:00" "08:35-10:10")

array_of_journey_purpose=("travel_to_hyderbad" "travel_to_Ranchi" "Travel_to_inderhome" "Parents_journey_fr_lagna" "parents_return_to_home" "Himadri_return_home" "parents_travel_fr_receiption" "Parents_return_home" "puri_darshan_inder" "trip_to_jalpaiguri" "reurn_to_howrah" "return_to_hyderbad")

array_date_for_each_journey=("19-11-2022" "23-11-2022" "23-11-2022" "23-11-2022" "24-11-2022"  "26-11-2022" "03-12-2022" "04-12-2022" "09-12-2022" "10-12-2022" "17-12-2022" "18-12-2022" "24-12-2022")

for (( i=0; i<=$(( ${#array_of_jouney[@]} -1 )); i++ ))
do
	echo -e "\n" =============================== ============= JOurmey $i starts here ================== ===============================
	echo ${array_of_jouney_people[i]} will be traveller for ${array_of_journey_purpose[i]}
	echo Hi, Your train name ${array_train_name[i]} with train no ${array_train_no[i]} is booked with seat ${array_seat_no[i]}.
	echo Journey is from place to: ${array_of_jouney[i]}  on date: ${array_date_for_each_journey[i]}
	echo Starting and ending time for train travelling is: ${array_of_time[i]}
	cur_date=`date +%d-%m-%y`
	month_num_cur_date=`date +%m`
	day_num_cur_date=`date +%d`

	month_num_journey_date=${array_date_for_each_journey[i]:3:2}
	day_num_journey_date=${array_date_for_each_journey[i]:0:2}

	echo Cuurent date details here : $cur_date, $month_num_cur_date, $day_num_cur_date
	echo Journey date detials here : ${array_date_for_each_journey[i]}, $month_num_journey_date, $day_num_journey_date
	
	(( month=10#$month_num_journey_date-10#$month_num_cur_date ))
	(( day=10#$day_num_journey_date-10#$day_num_cur_date ))
	(( total_day=(10#$month*30)+10#$day ))

	echo Considering every moth as 30 days. Days Calculation: $month, $day, $total_day

	if [ $total_day -gt 5 ]; then
		echo total_day -gt 5
	fi
done
