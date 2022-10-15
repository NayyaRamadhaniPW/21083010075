printf "Kamu suka makan apa ??\n"
printf "Terang bulan ?\n"
printf "Nasi Goreng ?\n"
printf "Mie ayam ?\n"

read makan

case "$makan" in 
  "Terang bulan")
    echo "Terang bulan coklat keju" 
    ;;
  "Nasi Goreng")
    echo "Nasi goreng seafood enak"
    ;;
  "Mie ayam")
    echo "Mie ayam pak bak suka banget"
    ;;
  *)
    echo "Aku ga suka itu semua"
    ;;
esac
