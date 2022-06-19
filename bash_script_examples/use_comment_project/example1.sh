#!/bin/bash

#=====  single line comment ===========
#!/bin/bash

# Add two numeric value
#((sum=25+35))
A=25
B=35
echo Normal syntax as we use for adding
SUM1=$A+$B
SUM2=$A + $B
((SUM2A=$A+$B))
#Print the result
echo sum for $A and $B is
echo $SUM1
echo $SUM2
echo $SUM2A

echo =============================
echo Using expr command with quotes
SUM3=`expr $A + $B`
#Print the result
echo sum for $A and $B is
echo $SUM3
echo =============================
echo Use expr command inclosed with brackets and start with dollar symbol.
SUM4=$(expr $A + $B)
#Print the result
echo sum for $A and $B is
echo $SUM4
echo =============================
echo directly with the shell.
SUM5=$(($A + $B))
#Print the result
echo sum for $A and $B is
echo $SUM5
echo =============================

