#mendeklarasikan distro 
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

#random distro 
let pilih=$RANDOM%5

#eksekusi skrip
echo "Saya memilih distro $pilih, ${distroLinux[$pilih]} !"

