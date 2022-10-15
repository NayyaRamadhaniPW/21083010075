#percabangan if.....else
a=18
b=7

if [ $a == $b ]
then
  echo "a sama dengan b"
elif [ $a -gt $b ]
then
  echo "a lebih besar dari b"
elif [ $a -lt $b ]
then
  echo "a lebih kecil dari b"
else
  echo "tidak ada kondisi yang memenuhi"
fi
