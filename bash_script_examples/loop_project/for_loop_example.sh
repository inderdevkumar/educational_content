#!/bin/bash

#=====  Multi line comments ===========


for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
#printf "\n


values=(0.31 0.18 0.33 1126.40 0.00 0.00)
total=${#values[*]}
for (( i=0; i<=$(( $total -1 )); i++ ))
do 
    echo -n "${values[$i]} "
done
