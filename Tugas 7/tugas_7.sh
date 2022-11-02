identitas() {
	parameter1=$a
	parameter2=$b
	echo "$parameter1"
	echo "$parameter2"
	
}

echo "Masukan Panjang:"
read a
echo "Masukan Lebar:"
read b
echo "Luas Persegi: "
let c=$a*$b
printf "$c"
printf "\n"

