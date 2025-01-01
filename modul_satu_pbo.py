# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/

# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini
class Buku:
    def __init__(self, judul, penulis, tahun_terbit, genre):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.genre = genre

    def deskripsi_buku(self):
        return f"'{self.judul}' adalah buku bergenre {self.genre} yang ditulis oleh {self.penulis} dan diterbitkan pada tahun {self.tahun_terbit}."

    def cek_genre(self, genre):
        if self.genre.lower() == genre.lower():
            return f"Buku '{self.judul}' termasuk dalam genre {genre}."
        else:
            return f"Buku '{self.judul}' bukan termasuk dalam genre {genre}."
