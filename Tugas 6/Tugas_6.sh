declare -a nilai
echo "Masukan:" ;
read angka

for ((i=0; i<$angka; i++))
do
   echo "Nilai IPS $((i+1)) :"
   read ips[$i];
   let total=$total+${ips[i]};
   let ipk=$total/$angka ;
done
echo "IPS Mahasiswa : " $total/$angka
echo "IPK Mahasiswa : " $ipk
