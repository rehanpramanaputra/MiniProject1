class TokoBuah:
    def __init__(self):
        self.daftar_buah ={'semangka': {'harga': 10000, 'stok': 20, 'jenis': 'semangka kuning', 'kualitas': 'Local'},
                            'anggur': {'harga': 15000, 'stok': 15, 'jenis': 'anggur hijau', 'kualitas': 'Impor'},
                            'jeruk': {'harga': 8000, 'stok': 25, 'jenis': 'jeruk purut', 'kualitas': 'local'},
                            'durian': {'harga': 12000, 'stok': 10, 'jenis': 'durian montong', 'kualitas': 'Impor'}}

    def tambah_buah(self, nama, harga, stok, jenis, kualitas):
        if nama not in self.daftar_buah:
            self.daftar_buah[nama] = {'harga': harga, 'stok': stok, 'jenis': jenis, 'kualitas': kualitas}
            print(f"{nama} berhasil ditambahkan ke dalam daftar buah.")
        else:
            print(f"{nama} sudah ada dalam daftar buah.")

    def lihat_daftar_buah(self):
        print("=========================== Daftar Buah di Toko =============================================")
        print("{:<15} {:<10} {:<10} {:<15} {:<30}".format("Nama", "Harga", "Stok", "Jenis", "Kualitas"))
        for nama, info in self.daftar_buah.items():
            print("{:<15} {:<10} {:<10} {:<15} {:<30}".format(nama, info['harga'], info['stok'], info['jenis'], info['kualitas']))

    def perbarui_buah(self, nama, harga=None, stok=None, jenis=None, kualitas=None):
        if nama in self.daftar_buah:
            if harga is not None:
                self.daftar_buah[nama]['harga'] = harga
            if stok is not None:
                self.daftar_buah[nama]['stok'] = stok
            if jenis is not None:
                self.daftar_buah[nama]['jenis'] = jenis
            if kualitas is not None:
                self.daftar_buah[nama]['kualitas'] = kualitas
            print(f"Informasi buah {nama} berhasil diperbarui.")
        else:
            print(f"{nama} tidak ditemukan dalam daftar buah.")

    def hapus_buah(self, nama):
        if nama in self.daftar_buah:
            del self.daftar_buah[nama]
            print(f"{nama} berhasil dihapus dari daftar buah.")
        else:
            print(f"{nama} tidak ditemukan dalam daftar buah.")


if __name__ == "__main__":
    toko = TokoBuah()

    while True:
        print("\nPilihan abang ku:")
        print("1. Tambah Buah")
        print("2. Lihat Daftar Buah")
        print("3. Perbarui Buah")
        print("4. Hapus Buah")
        print("5. Keluar")


        pilihan = input("pilih dulu gk sih: ")

        if pilihan == "1":
            nama = input("Masukkan nama buah: ")
            harga = int(input("Masukkan harga buah: "))
            stok = int(input("Masukkan stok buah: "))
            jenis = input("Masukkan jenis buah: ")
            kualitas = input("Masukkan kualitas buah: ")
            toko.tambah_buah(nama, harga, stok, jenis, kualitas)
        elif pilihan == "2":
            toko.lihat_daftar_buah()
        elif pilihan == "3":
            nama = input("Masukkan nama buah yang ingin diperbarui: ")
            harga = int(input("Masukkan harga baru buah: "))
            stok = int(input("Masukkan stok baru buah: "))
            jenis = input("Masukkan jenis baru buah: ")
            kualitas = input("Masukkan kualitas baru buah: ")
            toko.perbarui_buah(nama, harga, stok, jenis, kualitas)
        elif pilihan == "4":
            nama = input("Masukkan nama buah yang ingin dihapus: ")
            toko.hapus_buah(nama)
        elif pilihan == "5":
            print("Terima kasih! Sudah Datang TETAP MENYALA ABANG KU")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")


        