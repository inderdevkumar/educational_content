

#!/bin/sh

convertsecs() {
 ((h=${1}/3600))
 ((m=(${1}%3600)/60))
 ((s=${1}%60))
 printf "%02d:%02d:%02d\n" $h $m $s
}
TIME1="36"
TIME2="3610"
TIME3="91925"

echo $(convertsecs $TIME1)
echo $(convertsecs $TIME2)
echo $(convertsecs $TIME3)



convertsecs2() {
 h=$(bc <<< "${1}/3600")
 m=$(bc <<< "(${1}%3600)/60")
 s=$(bc <<< "${1}%60")
 printf "%02d:%02d:%05.2f\n" $h $m $s
}
echo $(convertsecs2 $TIME1)
echo $(convertsecs2 $TIME2)
echo $(convertsecs2 $TIME3)

