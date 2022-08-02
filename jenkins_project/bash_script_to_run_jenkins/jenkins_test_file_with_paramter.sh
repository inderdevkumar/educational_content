#!/usr/bin/env bash
echo
echo =================================
echo My first Jenkin Job
echo
echo =================================
echo Todays date time
date
echo
echo =================================
echo Find  sum  of $val_x and $val_y
sum_x_y=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]+ARGV[2]}' "$val_x" "$val_y"`

echo
echo =================================
echo Find  subtraction  of $val_x and $val_y
sub_x_y=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]-ARGV[2]}' "$val_x" "$val_y"`
echo
echo =================================
echo Find  multiplication  of $val_x and $val_y
mult_x_y=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]*ARGV[2]}' "$val_x" "$val_y"`
echo
echo =================================
echo Find  Division  of $val_x and $val_y
div_x_y=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]/ARGV[2]}' "$val_x" "$val_y"`
echo
echo =================================
echo
echo Sum is: $sum_x_y
echo Subtraction is: $sub_x_y
echo Multiplication is: $mult_x_y
echo Division is: $div_x_y
echo
echo =================================


