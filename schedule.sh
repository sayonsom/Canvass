#min=5
#max=10
#toy = jot -r 1 $min $max
#echo toy

a=0

while [ $a -lt 24 ]
do
   echo $a
   if [ $a -eq 5 ]
   then
      break
   fi
   a=`expr $a + 1`
done
