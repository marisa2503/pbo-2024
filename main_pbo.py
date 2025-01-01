# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py
from modul_satu_pbo import Buku


# Membuat objek Buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, "Fiksi")
buku2 = Buku("Atomic Habits", "James Clear", 2018, "Pengembangan Diri")

# Menggunakan fungsi yang ada di dalam class Buku
print(buku1.deskripsi_buku())
print(buku2.deskripsi_buku())

# Mengecek genre buku
print(buku1.cek_genre("Fiksi"))
print(buku2.cek_genre("Fiksi"))
