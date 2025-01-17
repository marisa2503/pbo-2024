class BankAccount:
    def __init__(self, pemilik, saldo=0):
        """Inisialisasi objek akun dengan pemilik dan saldo (default saldo 0)"""
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        """Menambahkan uang ke saldo"""
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setoran: Rp{jumlah}. Saldo baru: Rp{self.saldo}.")
        else:
            print("Jumlah setoran harus positif.")

    def tarik(self, jumlah):
        """Menarik uang dari saldo, jika saldo mencukupi"""
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Penarikan: Rp{jumlah}. Saldo baru: Rp{self.saldo}.")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi.")
        else:
            print("Jumlah penarikan harus positif.")

    def cek_saldo(self):
        """Menampilkan saldo terkini"""
        print(f"Saldo akun {self.pemilik}: Rp{self.saldo}")
