import sys 
total = []

#pembukaan     
print("="*45)
print("Selamat Datang Halaman utama Kasir Cafe EsJeruku")


#pilihan='y'
def menu() :
    #while pilihan=='y':
    print("\n")
    print("="* 45)
    print("Menu Utama Cafe EsJeruku ")
    #print("")
    print("="*45)
    print("Makanan Utama ")
    print("="*45)
    print(" 1. Cheese Cake Slice    : Rp. 23.000")
    print(" 2. Plain Croissant      : Rp. 28.000")
    print(" 3. Choco Croissant      : Rp. 32.000")
    print("="*45)
    print("Minuman (Tea, Coffe and Juice)")
    print("="*45)
    print("4. Black Cold Brew       : Rp. 14.000")
    print("5. Mocha Mint            : Rp. 10.000")
    print("6. Pineapple Juice       : Rp. 17.000")
    print("="*45)
    print("\n")
    pesanan= int(input("Masukan pesanan anda (makan): "))
##def harga_mkn():##
# daftar untuk pemilihan menu makanan 
    if pesanan == 1 : 
        jml_1= int(input("Masukan jumlah barang : "))
        t1 = 23000*jml_1
        total.append(t1)
        ask()
    elif pesanan == 2 : 
        jml_2= int(input("Masukan jumlah Barang: "))
        t2 = 28000*jml_2
        total.append(t2)
        ask()
    elif pesanan == 3:
        jml_3= int(input("Masukan jumlah barang:"))
        t3=32000*jml_3
        total.append(t3)
        ask()
    else : 
        print("Tidak ada di menu")
    return 

#daftar pemilihan menu minuman 
def harga_minum(): #harga minuman 
    minum = int(input("Masukan pesanan anda (minuman): "))
    if minum == 4 : 
        jml_4 = int(input("Masukan Jumlah minuman yang dipesan : "))
        t4 = 14000*jml_4 
        total.append(t4)
        ask()
    elif minum == 5 :
        jml_5 = int(input("Masukan Jumlah minuman yang dipesan :"))
        t5=10000*jml_5
        total.append(t5)
        ask()
    elif minum == 6 : 
        jml_6= int(input("Masukan Jumlah minuman yang dipesan :"))
        t6=17000*jml_6
        total.append(t6)
        ask()
    else : 
        print("Tidak ada di menu")
           

def ask(): 
    ask= input("apakah anda ingin pesan minum? [y/t]")
    if ask == "y" : 
        harga_minum()
    elif ask == "t":  
        akhir()
    else :
        print("-"*5, "PILIHAN SALAH", "-"*5)
        print("")      
#menu transaksi 
def pembayaran(): 
    print("\n")
    metode = input("pembayaran melalui tunai atau non tunai? ")
    if pembayaran == "tunai" :
        print("Anda dapat bayar langsung melalui kasir !")
    elif  pembayaran == "non tunai":
        print("Silahkan Scan Barcode ini") 
    #else :
     #   "TIDAK TERDAPAT PILIHAN TERSEBUT"
    
    #return
    print("\n", "-"*4,"TERIMA KASIH TELAH DATANG KE CAFE ESJERUKU", "-"*4)

def akhir():
    print("-"*51)
    print("-"*10,"STRUK PEMBELIAN CAFE ESJERUKU", "-"*10)
    for harga in total : 
        subtotal = sum(total)
        print("Sub Total  : ", subtotal)
        if (subtotal >= 25000) and (subtotal < 50000) : #belanja diatas 25k diskon 5% 
            diskon = subtotal * 5/100
            print("Diskon : Rp {:,}".format(int(diskon)).replace(",","."))
        elif (subtotal >= 50000) and (subtotal < 100000) : #belanja diatas 50k diskon 10%
            diskon = subtotal * 10/100
            print("Diskon : Rp {:,}".format(int(diskon)).replace(",","."))
        elif (subtotal > 100000) : # belanja diatas 100k diskon 30% 
            diskon = subtotal * 30/100
            print("Diskon : Rp {:,}".format(int(diskon)).replace(",","."))
        else : 
            diskon = 0
            print("Diskon : Rp {:,}".format(int(diskon)).replace(",","."))
        print("")
 #   pembayaran()
  #menghitung total pembelian
        print("Potongan Harga (Diskon): Rp {:,}".format(int(diskon)).replace(",","."))
        hasilakhir = subtotal - diskon 
        print("Total : Rp  {:,}".format(int(hasilakhir)).replace(",","."))
        
        
    #menghitung kembalian 
    bayar = int(input("Nominal Pembayaran: Rp. "))
    if hasilakhir <= bayar :
        kembalian = bayar - hasilakhir 
        print("Kembalian: Rp {:,}".format(int(kembalian)).replace(",","."))
    elif hasilakhir >= bayar : 
        kurang = hasilakhir - bayar
        print("Uang anda Kurang: Rp {:,}".format(int(kurang)).replace(",","."))      


menu()
pembayaran()
