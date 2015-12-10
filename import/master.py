"""
import module python

untuk dapat mengimpor modul yang berada pada direktori
diluar path default python, perlu ditambahakn file python
"__init__.py" di setiap sub folder. file ini digunakan sebagai
penanda bagi interpreter bahwa folder tersebut adalah sebuah
package module. file "__init__.py" tersebut dapat diisi
dengan source code atau biarkan file tersebut kosong,
"""

#sebagai contoh, hanya di impor fungsi pengurangan saja tanpa
#fungsi penambahan
from modul.aritmatika.penjumlahan_pengurangan import pengurangan

from modul.aritmatika.perkalian import *
from modul.lingkaran.rumus_lingkaran import *
from modul.segiempat.rumus_segiempat import *

"""
mengimport modul tidak harus selalu di import secara keseluruhan
modul dapat di import per-fungsi misalnya. contoh :

>>>> from modul.aritmatika.penjumlahan_pengurangan import penjumlahan

jika yang di impor hanya penjumlahan, maka fungsi pengurangan tidak
akan di impor, sehingga saat di eksekusi, akan menghasilkan error

dalam sebuah modul katakan modul "A", apabila dia mengimpor fungsi
atau modul lain katakan fungsi/modul "B". dan kemudian modul A
di impor oleh modul lain, sebut saja modul "C". maka otomatis modul
atau fungsi yang berada pada modul "B" akan ikut terimpor kedalam
modul "C" walaupun dalam modul "C" tidak mengimpor modul "B" SECARA 
LANGSUNG.

pada contoh source code ini, pada package aritmatika, modul
perkalian, di dalamnya di impor fungsi "penjumlahan" dari modul 
"penjumlahan_perkalian". sehingga, apabila modul ini, hanya mengimpor
fungsi "pengurangan" saja pada package "aritmatika", script ini
tetap dapat di eksekusi dengan baik meski tidak mengimpor fungsi 
"penjumlahan". karena fungsi penjumlahan sudah terimpor bersama
dengan modul perkalian. silahkan cek pada modul "perkalian.py"
di package "aritmatika"
"""

def runFirst():
	inputan1 = input ("Masukkan bilangan pertama\t: ")
	inputan2 = input ("Masukkan bilangan kedua\t\t: ")

	dijumlah = penjumlahan(inputan1,inputan2)
	dikali = perkalian(inputan1,inputan2)
	dikurangi = pengurangan(inputan1,inputan2)
	
	print "hasil dijumlah\t: ", dijumlah
	print "hasil dikali\t: ", dikali
	print "hasil dikurangi\t: ",dikurangi
	
	print "\n\nSesi Bangun Ruang"
	print "LINGKARAN\n"
	print "Menghitung luas dan keliling lingkaran berdasarkan input jari-jari"
	jari2 = input("Jari-jari lingkaran\t: ")
	print "\n"
	print "PERSEGI\n"
	print "Menghitung luas dan keliling lingkaran berdasarkan input sisi"
	sisi = input("Sisi Persegi\t: ")
	
	hasilLuasPersegi = luasPersegi(sisi)
	hasilKelilingPersegi = kelilingPersegi(sisi)
	hasilLuasLingkaran = luasLingkaran(jari2)
	hasilKelilingLingkaran = kelilingLingkaran(jari2)

	print "\n"
	print "keliling lingkaran\t: ", hasilKelilingLingkaran
	print "luas lingkaran\t\t: ", hasilLuasLingkaran
	print "keliling persegi\t: ",hasilKelilingPersegi
	print "luas lingkaran\t\t: ",hasilLuasPersegi
	
	print "\n\nakhir dari script"
	input ("Silahkan tekan enter untuk mengakhiri")
	
runFirst()
