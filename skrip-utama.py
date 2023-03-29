#!/usr/bin/env python
# coding: utf-8

# In[11]:


from luas.persegi import *
from luas.persegi_panjang import *
from luas.segitiga import *
from luas.lingkaran import *
from luas.trapesium import *
from luas.jajar_genjang import *
from volume.kubus import *
from volume.balok import *
from volume.tabung import *
from volume.kerucut import *
from volume.limas import *
from volume.prisma import *

while True:
    print(" ")
    print("----- SELAMAT DATANG DI PROGRAM PERHITUNGAN LUAS DAN VOLUME -----")
    print(" ")
    print("Silahkan Pilih Opsi Dibawah Ini : ")
    print("1. Menghitung Luas 2 Dimensi")
    print("2. Menghitung Volume 3 Dimensi")
    print("3. Keluar")
    print(" ")
    pilih = input("Pilih Opsi (1, 2 DAN 3) : ")
    print(" ")

    if pilih == "1":
        print("----- 2 DIMENSI -----")
        print("1. Persegi")
        print("2. Persegi panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar genjang")
        print("6. Trapesium")
        print(" ")
        
        dua_dimensi = input("Pilih bangun datar yang mau dicari : ") #input opsi 2 dimensi
        
        if dua_dimensi == "1":
            sisi_persegi = float(input("Panjang Sisi : "))
            print(persegi(sisi_persegi)) #import peregi
            
        elif dua_dimensi == "2":
            panjang_pp = float(input("Masukkan Panjang : "))
            lebar_pp = float(input("Masukkan Lebar : "))
            print(persegi_panjang(panjang_pp, lebar_pp)) #import peregi panjang
    
        elif dua_dimensi == "3":
            alas_segiriga = float(input("Masukkan Alas : "))
            tinggi_segitiga = float(input("Masukkan Tinggi : "))
            print(segitiga(alas_segiriga, tinggi_segitiga)) #import segitiga
            
        elif dua_dimensi == "4":
            jari_ling = float(input("Masukkan jari-jari : "))
            print(lingkaran(jari_ling)) #import lingkaran
            
        elif dua_dimensi == "5":
            alas_jg = float(input("Masukkan Alasnya : "))
            tinggi_jg = float(input("Masukkan Tinggi : "))
            print(jajar_genjang(alas_jg, tinggi_jg)) #import jajar genjang
            
        elif dua_dimensi == "6":
            atas = float(input("Masukkan panjang Atas : "))
            bawah = float(input("Masukkan sisi Bawah : "))
            tinggi_trap = float(input("Masukkan Tinggi : "))
            print(trapesium(atas, bawah, tinggi_trap)) #import trapesium
            


        else: print("******Mohon maaf pilih sesuai yang tertera******")
        
    elif pilih == "2":
        print("----- 3 DIMENSI -----")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Limas")
        print("6. Prisma")
        print(" ")

        tiga_dimensi=input("Pilih bangun ruang yang mau dicari : ") #input opsi 3 dimensi
        
        if tiga_dimensi == "1":
            sisi_kubus = float(input("masukkan panjang sisi : "))
            print(kubus(sisi_kubus)) #import kubus
            
        elif tiga_dimensi == "2":
            panjang_balok = float(input("masukkan panjangnya : "))
            lebar_balok = float(input("masukkan lebarnya : "))
            tinggi_balok = float(input("tinggi : "))
            print(balok(panjang_balok, lebar_balok, tinggi_balok)) #import balok
            
        elif tiga_dimensi == "3":
            jari_tabung = float(input("masukkan jari-jarinya : "))
            tinggi_tabung = float(input("masukkan tingginya : "))
            print(tabung(jari_tabung, tinggi_tabung)) #import tabung
            
        elif tiga_dimensi == "4":
            jari_kerucut = float(input("masukkan jari-jarinya : "))
            tinggi_kerucut = float(input("masukkan tingginya : "))
            print(kerucut(jari_kerucut, tinggi_kerucut)) #import kerucut
            
        elif tiga_dimensi == "5":
            lalas_limas = float(input("masukkan luas alas : "))
            tinggi_limas = float(input("masukkan tinggi : "))
            print(limas(lalas_limas, tinggi_limas)) #import limas
            
        elif tiga_dimensi == "6":
            lalas_prisma = float(input("masukkan luas alas : "))
            tinggi_prisma = float(input("masukkan tinggi : "))
            print(prisma(lalas_prisma, tinggi_prisma)) #import prisma
     
    elif pilih == "3":
        kembali = input("Apakah anda ingin melanjutkan? (yes/no) ")
        if kembali == "no":
            break
        elif kembali == "yes":
            continue       
        
        else: print("******Mohon maaf pilih sesuai yang tertera******")
            
    else : print("******Mohon maaf pilih sesuai yang tertera******")
       
print("Terima kasih telah menggunakan program kami")


# In[ ]:




