echo -n "Tolong masukan angka positif: ";
read angka;

a=0

while [ ! "$angka" -lt $a ] || [ "$angka" -gt 20 ]
do

  echo $angka
  angka=$(($angka - 2))

done
