#latihan soal percabangan 
x=90 
y=2

#operasi matematika
a= let a=x*y
b= let b=x%y

#menggunakan percabangan if...else 
if [ $a -eq $b ]
then
  echo "operasi a sama dengan b"
elif [ $b -le $a ]
then
  echo "operasi b lebih kecil dari a"
else
  echo "tidak ada yang memenuhi"
fi


