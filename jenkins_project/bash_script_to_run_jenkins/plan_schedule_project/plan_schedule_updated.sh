#!/bin/bash


 Red=$'\e[1;31m'
 Green=$'\e[1;32m'
 Yellow=$'\e[1;33m'

train_name_del="BBS Rajdhani"
train_num_del="12345"
train_name_bbs_kqr="Purushottam Express"
train_num_bbs_kqr="12346"
train_name_kqr_bbs="Nandankanan Express"
train_num_kqr_bbs="12347"
train_name_kqr_puri="Purushottam Express"
train_num_kqr_puri="12348"
train_name_puri_njp="Ghy SC Express"
train_num_puri_njp="12349"
train_name_njp_hwr="Saraighat Express"
train_num_njp_hwr="12350"
train_name_hwr_hyd="SC Express"
train_num_hwr_hyd="12351"




echo ###############################################
echo "These are the scheduled plans for your Journey ^^^ WELCOME"
echo ###############################################
echo "***  1.Inder's Journey from Delhi to KQR on 23rd November *** "


echo "Say Yes if train is booked else No"
read del_book

if [[  ( $del_book  == "Yes" || $del_book == "yes")  ]]; then
echo "Please enter Train Boggy with seat Number:   "
read del_kqr_seat_num
     if [[  ( $del_kqr_seat_num  == "*wl*" || $del_kqr_seat_num == "WL" )  ]]; then
     echo Your Train is booked with Waiting List $del_kqr_seat_num 
     

     echo Your Train name $train_name_del with train number $train_num_del is booked with seat $del_kqr_seat_num
     echo And your  journey is from Delhi to Koderma on 23rd Nov 2022.

     else
    

     echo Your Train name $train_name_del with train number $train_num_del is booked with seat $del_kqr_seat_num
     echo journey is from Delhi to Koderma on 23rd Nov 2022.

     fi     
else	     
echo "$Red Train is not booked yet...Book it soon !!!"
fi     

echo "***************      Next Journey Starts Here    ****************"

echo "***  2. Parents's Journey from BBSR to KQR on 23rd November *** "

echo "Say Yes if train is booked else No"
read bbs_kqr_book

if [[  ( $bbs_kqr_book  == "Yes" || $bbs_kqr_book  == "yes")  ]]; then



echo "Please Enter the Train Boggy with Seat Number : "
read bbs_kqr_seat_num

if [[  ( $bbs_kqr_seat_num  == "*wl*" || $bbs_kqr_seat_num == "WL" )  ]]; then
     echo Your Train is booked with Waiting List $bbs_kqr_seat_num


     echo Your Train name $train_name_del with train number $train_num_del is booked with seat $bbs_kqr_seat_num
     echo And your  journey is from BBSR to Koderma on 23rd Nov 2022.

     else


     echo Your Train name $train_name_del with train number $train_num_del is booked with seat $bbs_kqr_seat_num
     echo journey is from BBSR  to Koderma on 23rd Nov 2022.

     fi


else
echo "Train is not booked yet..."
fi


echo "***  3. Parents's Return Journey from KQR to BBSR on 24th November *** "

echo "Say Yes if train is booked else No"
read kqr_bbs_book

if [[  ( $kqr_bbs_book  == "Yes" || $kqr_bbs_book  == "yes")  ]]; then
echo "Please Enter the Train Boggy with Seat Number : "
read kqr_bbs_seat_num
else
echo "Train is not booked yet..."
fi



echo "***  4.  Journey from KQR to Puri on 9th Dec *** "

echo "Say Yes if train is booked else No"
read kqr_puri_book

if [[  ( $kqr_puri_book  == "Yes" ||  $kqr_puri_book  == "yes" )  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read kqr_puri_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  5.  Journey from Puri to NJP on 10th Dec *** "

echo "Say Yes if train is booked else No"
read puri_njp_book

if [[  ( $puri_njp_book  == "Yes" || $puri_njp_book  == "yes")  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read puri_njp_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  6.  Journey from NJP to Howrah on 17th Dec *** "

echo "Say Yes if train is booked else No"
read njp_hwrah_book

if [[  ( $njp_hwrah_book  == "Yes" || $njp_hwrah_book  == "yes")  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read njp_howrh_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  7.  Journey from  Howrah to hyderabad on 18th Dec *** "

echo "Say Yes if train is booked else No"
read hwr_hyd_book

if [[  ( $hwr_hyd_book  == "Yes"  || $hwr_hyd_book  == "yes")  ]]; then
echo "Please Enter the Train boggy with  Seat Number : "
read hwr_hyd_seat_num
else
echo "Train is not booked yet..."
fi



