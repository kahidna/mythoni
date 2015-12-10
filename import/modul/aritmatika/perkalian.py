"""
sebagai contoh, hanya mengimpor fungsi "penjumlahan"
kemudian modul "perkalian" ini akan dipanggil di modul
"master".

dokumentasi silahkan lihat di file "master.py"
"""
from penjumlahan_pengurangan import penjumlahan

def perkalian(operand1, operand2):
	hasil = operand1 * operand2
	
	return hasil
