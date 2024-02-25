from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Inisialisasi Dictionary untuk data akun, voucher, dan buah
data_akun = {'Nama': '', 'PIN': '', 'saldo': 30000, 'e-pay': 0, 'member': ''}
data_voucher = {'kode': 'Voucher30', 'nama_voucher': 'Diskon30', 'persentase_diskon': 30, 'status': 'Aktif'}
data_buah = {'Apel': 5000, 'Jeruk': 7000, 'Anggur': 15000, 'Mangga': 10000}

# Inisialisasi List untuk menyimpan data transaksi
transaksi_list = []

# Fungsi untuk membuat akun
def buat_akun():
    print("=== Membuat Akun ===")
    data_akun['Nama'] = input("Masukkan nama Anda: ")
    data_akun['PIN'] = input("Buat PIN untuk login: ")
    data_akun['member'] = 'Gratisan'  # Semua akun baru dianggap gratisan secara default

# Fungsi untuk login
def login():
    entered_pin = input("Masukan nama Anda:")
    entered_pin = input("Masukkan PIN Anda: ")
    if entered_pin == data_akun['PIN']:
        print("Login berhasil!")
    else:
        print("PIN salah. Login gagal.")
        return False
    return True

# Fungsi untuk top up e-pay
def top_up():
    amount = int(input("Masukkan jumlah uang yang ingin di-top up: "))
    data_akun['saldo'] -= amount
    data_akun['e-pay'] += amount
    print(f"Top up berhasil! Saldo Anda sekarang: {data_akun['saldo']}, e-pay Anda: {data_akun['e-pay']}")
    # Menyimpan data transaksi top-up
    transaksi_list.append(('Top Up e-pay', amount))

# Fungsi untuk registrasi member VIP
def registrasi_member():
    if data_akun['member'] == 'Gratisan':
        print("Anda berhasil menjadi Member VIP!")
        data_akun['member'] = 'VIP'
    else:
        print("Anda sudah menjadi Member VIP sebelumnya.")

# Fungsi untuk pembelian dengan e-pay
def beli_dengan_epay(harga_barang):
    if data_akun['e-pay'] >= harga_barang:
        data_akun['e-pay'] -= harga_barang
        print(f"Pembelian berhasil! e-pay Anda sekarang: {data_akun['e-pay']}")
        # Menyimpan data transaksi pembelian dengan e-pay
        transaksi_list.append(('Pembelian dengan e-pay', harga_barang))
    else:
        print("Saldo e-pay tidak mencukupi. Silakan top up terlebih dahulu.")

# Fungsi untuk pembelian dengan diskon
def beli_dengan_diskon(harga_barang):
    if data_akun['member'] == 'VIP':
        harga_setelah_diskon = harga_barang * 0.7  # Diskon 30% untuk Member VIP
        print(f"Pembelian berhasil! Harga setelah diskon: {harga_setelah_diskon}")
        # Menyimpan data transaksi pembelian dengan diskon
        transaksi_list.append(('Pembelian dengan diskon', harga_setelah_diskon))
    else:
        print(f"Pilih metode pembayaran:")
        print("1. e-pay")
        print("2. Voucher Diskon")
        metode_pembayaran = int(input("Masukkan pilihan metode pembayaran: "))
        if metode_pembayaran == 1:
            beli_dengan_epay(harga_barang)
        elif metode_pembayaran == 2:
            beli_dengan_voucher(harga_barang)
        else:
            print("Pilihan tidak valid. Pembelian dibatalkan.")

# Fungsi untuk pembelian dengan voucher
def beli_dengan_voucher(harga_barang):
    voucher_code = input("Masukkan kode voucher: ")
    if voucher_code == data_voucher['kode'] and data_voucher['status'] == 'Aktif':
        diskon = harga_barang * (data_voucher['persentase_diskon'] / 100)
        harga_setelah_diskon = harga_barang - diskon
        print(f"Pembelian berhasil dengan diskon voucher! Harga setelah diskon: {harga_setelah_diskon}")
        # Menyimpan data transaksi pembelian dengan diskon voucher
        transaksi_list.append(('Pembelian dengan diskon voucher', harga_setelah_diskon))
    else:
        print("Voucher tidak valid atau sudah tidak aktif.")

# Fungsi untuk menampilkan daftar buah
def tampilkan_daftar_buah():
    table = PrettyTable()
    table.field_names = ["No", "Nama Buah", "Harga"]
    
    no = 1
    for nama_buah, harga in data_buah.items():
        table.add_row([no, nama_buah, harga])
        no += 1
    
    print(table)

# Fungsi untuk menampilkan chart transaksi
def tampilkan_chart():
    labels = [transaksi[0] for transaksi in transaksi_list]
    amounts = [transaksi[1] for transaksi in transaksi_list]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, amounts, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Jenis Transaksi')
    plt.ylabel('Jumlah (Rp)')
    plt.title('Grafik Transaksi')
    plt.show()

# Fungsi utama untuk melakukan transaksi
def transaksi():
    while True:
        print("\nMenu Utama:")
        print("1. Login")
        print("2. Buat Akun")
        print("3. Keluar")
        
        pilihan_utama = int(input("Masukkan pilihan: "))

        if pilihan_utama == 1:
            if not login():
                continue
            break
        elif pilihan_utama == 2:
            buat_akun()
        elif pilihan_utama == 3:
            print("Terima kasih. Selamat tinggal.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    while True:
        print("\nMenu Transaksi:")
        print("1. Top Up e-pay")
        print("2. Registrasi Member VIP")
        print("3. Tampilkan Daftar Buah")
        print("4. Pembelian Barang")
        print("5. Tampilkan Chart Transaksi")
        print("6. Selesai Transaksi")
        
        pilihan = int(input("Masukkan pilihan menu: "))

        if pilihan == 1:
            top_up()
        elif pilihan == 2:
            registrasi_member()
        elif pilihan == 3:
            tampilkan_daftar_buah()
        elif pilihan == 4:
            if data_akun['e-pay'] == 0:
                print("Saldo e-pay Anda kosong. Silakan top up terlebih dahulu.")
                continue
            nama_buah = input("Masukkan nama buah yang ingin dibeli: ")
            if nama_buah in data_buah:
                harga_barang = data_buah[nama_buah]
                beli_dengan_diskon(harga_barang)
            else:
                print("Buah tidak ditemukan.")
        elif pilihan == 5:
            tampilkan_chart()
        elif pilihan == 6:
            print("Terima kasih telah bertransaksi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memulai transaksi
transaksi()
