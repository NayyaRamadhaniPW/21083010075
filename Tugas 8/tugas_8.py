from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
    if (i-1)/2 == 0:
        print(i+1, "Genap-Punya ID proses", getpid())
    else : 
        print(i+1, "Ganjil-Punya ID proses", getpid())

    sleep(1)

#sekuensial 
print("angka:")
angka=int(input())
print("sekuensial")

sekuensial_awal = time()

for i in range(angka):
    cetak(i)

sekuensial_akhir = time()

#kelas proses
print("multiprocessing.Process")

kumpulan_proses = []

process_awal = time()

for i in range(angka):
    p = Process(target=cetak,args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()


process_akhir = time()

print("multiprocessing.Pool")

pool_awal = time()

pool = Pool()
pool.map(cetak, range(0,angka))
pool.close()


pool_akhir = time()

print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("waktu eksekusi Pool:", pool_akhir - pool_awal, "detik")



