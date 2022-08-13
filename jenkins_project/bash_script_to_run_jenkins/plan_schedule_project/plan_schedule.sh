#!/bin/bash
echo ###############################################
echo "These are the scheduled plans for your Journey ^^^ WELCOME"
echo ###############################################
echo "***  1.Inder's Journey from Delhi to KQR on 23rd November *** "
echo "Say Yes if train is booked else No"
read del_book

if [[  ( $del_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with Seat Number : "
read del_kqr_seat_num
else
echo "Train is not booked yet..."
fi     

echo "***  2. Parents's Journey from BBSR to KQR on 23rd November *** "

echo "Say Yes if train is booked else No"
read bbs_kqr_book

if [[  ( $bbs_kqr_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with Seat Number : "
read bbs_kqr_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  3. Parents's Return Journey from KQR to BBSR on 24th November *** "

echo "Say Yes if train is booked else No"
read kqr_bbs_book

if [[  ( $kqr_bbs_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with Seat Number : "
read kqr_bbs_seat_num
else
echo "Train is not booked yet..."
fi



echo "***  4.  Journey from KQR to Puri on 9th Dec *** "

echo "Say Yes if train is booked else No"
read kqr_puri_book

if [[  ( $kqr_puri_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read kqr_puri_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  5.  Journey from Puri to NJP on 10th Dec *** "

echo "Say Yes if train is booked else No"
read puri_njp_book

if [[  ( $puri_njp_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read puri_njp_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  6.  Journey from NJP to Howrah on 17th Dec *** "

echo "Say Yes if train is booked else No"
read njp_hwrah_book

if [[  ( $njp_hwrah_book  == "Yes")  ]]; then
echo "Please Enter the Train Boggy with  Seat Number : "
read njp_howrh_seat_num
else
echo "Train is not booked yet..."
fi


echo "***  7.  Journey from  Howrah to hyderabad on 18th Dec *** "

echo "Say Yes if train is booked else No"
read hwr_hyd_book

if [[  ( $hwr_hyd_book  == "Yes")  ]]; then
echo "Please Enter the Train boggy with  Seat Number : "
read hwr_hyd_seat_num
else
echo "Train is not booked yet..."
fi



