#!/bin/bash
echo "Enter first number"
read x
echo "Enter second number"
read y
(( sum=x+y ))
(( difference=x-y ))
(( multiplication=x*y ))
(( Divison=x/y ))
divide_with_dec=`awk -- 'BEGIN{printf "%.2f\n", ARGV[1]/ARGV[2]}' "$x" "$y"`

echo "The result of addition=$sum"
echo "The result of difference=$difference"
echo "The result of multiplication=$multiplication"
echo "The result of divison=$Divison"
echo "The result of divison with decimal=$divide_with_dec"
