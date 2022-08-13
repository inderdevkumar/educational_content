#!/bin/bash
echo ###############################################
echo "These are the scheduled plans for your Journey ^^^ WELCOME"
echo ###############################################
echo "***  1.Inder's Journey from Delhi to KQR on 23rd November *** "
echo "Say Yes if train is booked else No"
read del_book

if [[  ( $del_book  == "Yes")  ]]; then
echo "Please Enter the Train Seat Number : "
read seat_num1
else
echo "Train is not booked yet..."
fi     

echo "***  2. Parents's Journey from BBSR to KQR on 23rd November *** "

echo "Say Yes if train is booked else No"
read bbs_kqr_book

if [[  ( $bbs_kqr_book  == "Yes")  ]]; then
echo "Please Enter the Train Seat Number : "
read seat_num2
else
echo "Train is not booked yet..."
fi


echo "***  3. Parents's Return Journey from KQR to BBSR on 24th November *** "

echo "Say Yes if train is booked else No"
read kqr_bbs_book

if [[  ( $kqr_bbs_book  == "Yes")  ]]; then
echo "Please Enter the Train Seat Number : "
read seat_num3
else
echo "Train is not booked yet..."
fi



echo "***  4.  Journey from KQR to Puri on 9th Dec *** "

echo "Say Yes if train is booked else No"
read kqr_puri_book

if [[  ( $kqr_puri_book  == "Yes")  ]]; then
echo "Please Enter the Train Seat Number : "
read seat_num4
else
echo "Train is not booked yet..."
fi



echo "***  4.  Journey from KQR to Puri on 9th Dec *** "

echo "Say Yes if train is booked else No"
read kqr_puri_book

if [[  ( $kqr_puri_book  == "Yes")  ]]; then
echo "Please Enter the Train Seat Number : "
read seat_num4
else
echo "Train is not booked yet..."
fi



