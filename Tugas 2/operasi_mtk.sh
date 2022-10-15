a=20 
b=7

#Memakai let 
let jumlah=$a+$b
let kurang=$b-$a
let kali=$a*$b

#bila memakai expr
bagi='expr $a/$b'

#memakai perintah substitusi 
mod=$(($a%$b))

echo "a+b=$jumlah"
echo "a-b=$kurang"
echo "a*b=$kali"
echo "a/b=$bagi"
echo "a%b=$mod"

b=$a

echo "a=$a"
echo "b=$b"

