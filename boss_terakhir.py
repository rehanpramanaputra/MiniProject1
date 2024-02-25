import csv
import pwinput
from prettytable import PrettyTable
from datetime import datetime, timedelta

tabel_kamar = PrettyTable()

# untuk update data kamar ke tabel22
def refresh_table_kamar():
    tabel_kamar.clear()
    tabel_kamar.title = "Murah Meriah Muntah"
    if user_type == "normal":
        tabel_kamar.field_names = ["Nomor", "Jenis", "Harga Bulanan", "Pemilik"]
        for kamar in data_kamar:
            # replace = ubah string yang ada di dalam string dengan string lain
            # bingung kan bacanya? gampang aja kok
            # contoh nie:
            # "anjing".replace("njing", "su")
            # output: "asu"
            if kamar["ketersediaan"] == "tersedia":
                tabel_kamar.add_row([kamar["nomor"], kamar["jenis"], format_uang(kamar["harga bulanan"]), kamar["pemilik"]])
    else:
        tabel_kamar.field_names = ["Nomor", "Jenis", "Harga Bulanan", "Pemilik", "Ketersediaan"]
        for kamar in data_kamar:
            tabel_kamar.add_row([kamar["nomor"], kamar["jenis"], kamar["harga bulanan"], kamar["pemilik"], kamar["ketersediaan"]])


# ya tanggal harini
today = datetime.now()

# strftime =  string format time (ubah objek datetime ke bentuk string dalam format tertentu)
# Q: yg persen-persen tu apa banh?
# A: format tanggal. d=day (tgl), m=month (bulan), Y=year (tahun), H=hour (jam), M=minute (menit) // formatnya masih banyak lagi
tanggal = today.strftime("%d/%m/%Y %H:%M")

# Q: split ni apa?
# A: misah string jadi list, contohnya nih ngubah "aku/gila" jadi ["aku","gila"]
tahun, bulan = (today.strftime("%Y/%m")).split('/')

# timedelta itu untuk nambah waktu ke tanggal, jadi yang di bawah ni tuh tanggal setelah 30 hari
tenggat = (today+timedelta(days=30)).strftime("%d/%m/%Y %H:%M")

#-----------load csv-----------#
def load_data():
    # global untuk bikin variable yang *dibuat* di dalam function (def) bisa dipakai diluar function
    global data_kamar, data_user, userpass, data_pemasukan, adminpass
    try:
        data_kamar = []
        with open("data_kamar.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_kamar.append({"nomor": row[0], "jenis": row[1], "harga bulanan": int(row[2]), "ketersediaan": row[3], "pemilik": row[4]})
    except FileNotFoundError:
        # data kamar default ketika file tidak ditemukan
        data_kamar = [
            {"nomor": "101", "jenis": "Tunggal", "harga bulanan": 250000, "ketersediaan": "tersedia", "pemilik": ""},
            {"nomor": "102", "jenis": "Tunggal", "harga bulanan": 250000, "ketersediaan": "tersedia", "pemilik": ""},
            {"nomor": "201", "jenis": "Ganda", "harga bulanan": 400000, "ketersediaan": "tersedia", "pemilik": ""},
            {"nomor": "202", "jenis": "Ganda", "harga bulanan": 400000, "ketersediaan": "tersedia", "pemilik": ""}
        ]
        with open("data_kamar.csv", 'w', newline='') as file:
            fieldnames = ["nomor", "jenis", "harga bulanan", "ketersediaan", "pemilik"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for kamar in data_kamar:
                writer.writerow(kamar)

    data_user = []
    try:
        with open("data_user.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_user.append({"username": row[0], "nomor kamar": row[1], "terakhir bayar": row[2], "tenggat": row[3], "lunas": row[4], "saldo": int(row[5])})
    except FileNotFoundError:
        open("data_user.csv", 'w', newline='')

    userpass = []
    try:
        with open("userpass.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                userpass.append({"username": row[0], "password": row[1]})
    except FileNotFoundError:
        open("userpass.csv", 'w', newline='')

    data_pemasukan = []
    try:
        with open("data_pemasukan.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_pemasukan.append({"tahun": row[0], "bulan": row[1], "pemasukan": int(row[2])})
    except:
        with open("data_pemasukan.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tahun, bulan, 0])
    
    adminpass = {}
    try:
        with open("adminpass.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                adminpass = {"username": row[0], "password": row[1]}
    except FileNotFoundError:
        # username & password admin default ketika file tidak ditemukan
        adminpass = {"username":"admin", "password":"admin86"}
        with open("adminpass.csv", 'w', newline='') as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(adminpass)
#------------------------------#

load_data()

# save data ke file
def simpan_data():
    with open("data_user.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for user in data_user:
            writer.writerow([user["username"], user["nomor kamar"], user["terakhir bayar"], user["tenggat"], user["lunas"], user["saldo"]])

    with open("data_kamar.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for kamar in data_kamar:
            writer.writerow([kamar["nomor"], kamar["jenis"], kamar["harga bulanan"], kamar["ketersediaan"], kamar["pemilik"]])
    
    with open("data_pemasukan.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for data in data_pemasukan:
            writer.writerow([data["tahun"], data["bulan"], data["pemasukan"]])
    
    with open("userpass.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for akun in userpass:
            writer.writerow([akun["username"], akun["password"]])
    
    with open("adminpass.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adminpass["username"], adminpass["password"]])

simpan_data()
load_data()

# pengganti function input()
# - handle input biar gak error pas pencet copy di terminal
# - bisa batasi input supaya cuman bisa integer (pakai "int" di parameter 2)
# - bisa batasi input supaya cuman bisa digit (pakai "digit" di parameter 2)
# - untuk print error yg gk di handle tanpa bikin program berenti
def inputhandler(prompt, inputtype="str"):
    while True:
        try:
            if inputtype == "str":
                userinput = input(prompt)
            elif inputtype == "int":
                userinput = int(input(prompt))
            elif inputtype == "digit":
                userinput = input(prompt)
                if not userinput.isdigit():
                    print("Input hanya bisa berupa angka\n")
                    inputhandler(prompt)
            return userinput
        except KeyboardInterrupt:
            print("\nGabisa bikin error ctrl+c ye\n")
        except ValueError:
            print("Input hanya bisa berupa integer\n")
        except Exception as error:
            print(f"Error baru nih: {error}\n")

def format_uang(nominal):
    return f"Rp{nominal:,}".replace(',','.')

# tipe user (normal/admin)
user_type = ''

#--------------Admin--------------#
def tambah_kamar():
    while True:
        nomor = inputhandler("Nomor kamar: ", "digit")
        if any(kamar["nomor"] == nomor for kamar in data_kamar):
            print("kamar dah ada\n")
        else:
            break
    
    print("\nJenis Kamar")
    print("[1] Tunggal")
    print("[2] Ganda")
    while True:
        pilihan = inputhandler("Pilihan: ")
        if pilihan == '1':
            jenis = "Tunggal"
            break
        elif pilihan == '2':
            jenis = "Ganda"
            break
        else:
            print("bungul")
            
    harga = int(inputhandler("Harga bulanan: ", "digit"))
    
    data_kamar.append({"nomor": nomor, "jenis": jenis, "harga bulanan": harga, "pemilik": "", "ketersediaan": "tersedia"})
    # sort = urut list/dict dari angkah terkecil
    # lambda = mirip def, tapi tanpa nama function
    data_kamar.sort(key=lambda kamar: kamar["nomor"])
    simpan_data()
    refresh_table_kamar()
    print(tabel_kamar)
    print(f"Berhasil menambahkan kamar {nomor} ke data kamar")

def edit_kamar():
    print(tabel_kamar)
    while True:
        nomor = inputhandler("Nomor kamar: ", "digit")
        if any(kamar["nomor"] == nomor for kamar in data_kamar):
            break
        else:
            print("gaada kamar itu lek\n")
    
    print("\nJenis Kamar")
    print("[1] Tunggal")
    print("[2] Ganda")
    while True:
        pilihan = inputhandler("Pilihan: ")
        if pilihan == '1':
            jenis = "Tunggal"
            break
        elif pilihan == '2':
            jenis = "Ganda"
            break
        else:
            print("tegaga")

    harga = int(inputhandler("Harga bulanan: ", "digit"))

    for kamar in data_kamar:
        if kamar["nomor"] == nomor:
            kamar["jenis"] = jenis
            kamar["harga bulanan"] = harga
            simpan_data()
            refresh_table_kamar()
            print(tabel_kamar)
            print(f"Berhasil mengubah data dari kamar {nomor}")

def hapus_kamar():
    print(tabel_kamar)
    while True:
        nomor = inputhandler("Nomor kamar: ", "digit")
        if any(kamar["nomor"] == nomor for kamar in data_kamar):
            break
        else:
            print("gaada kamar itu lek\n")
        
    for kamar in data_kamar:
        if kamar["nomor"] == nomor:
            if kamar["pemilik"] != '':
                for user in data_user:
                    if user["username"] == kamar["pemilik"]:
                        kamar["ketersediaan"] = "pending"
                        simpan_data()
                        print("menunggu user untuk berhenti menyewa")
            else:
                data_kamar.remove(kamar)
                simpan_data()
                refresh_table_kamar()
                print("kamar dihapus")

# ku rapiin nanti
def menu_admin():
    print(f"\n{'='*10} Menu Admin (ngerinya) {'='*10}")
    while True:
        print("[1] Lihat kamar")
        print("[2] Tools")
        print("[3] Data user")
        print("[4] Pemasukkan")
        print("[5] Pengaturan akun")
        print("[6] Keluar")
        pilihan = inputhandler("Pilihan: ")
        
        if pilihan == '1':
            print(tabel_kamar)
        elif pilihan == '2':
            while True:
                print(f"\n{'='*10} Tools {'='*10}")
                print("[1] Tambah kamar")
                print("[2] Edit data kamar")
                print("[3] Hapus data kamar")
                print("[4] Kembali")
                pilihan = inputhandler("Pilihan: ")
                if pilihan == '1':
                    tambah_kamar()
                elif pilihan == '2':
                    edit_kamar()
                elif pilihan == '3':
                    hapus_kamar()
                elif pilihan == '4':
                    menu_admin()
                    break
                else:
                    print("Pilihan tidak valid!\n")

        elif pilihan == '3':
            while True:
                print(f"\n{'='*10} Data User {'='*10}")
                print("[1] Cari berdasar username")
                print("[2] Liat yang ngutang")
                print("[3] Liat yang udah bayar")
                print("[4] Kembali")
                pilihan = inputhandler("Pilihan: ")
                if pilihan == '1':
                    username = inputhandler("Siapa: ")
                    lihat_akun(username)
                elif pilihan == '2':
                    table = PrettyTable()
                    table.title = "Penunggak Hutang"
                    table.field_names = ["Nama", "Nomor kamar", "Tenggat", "Tagihan"]
                    
                    ada = False
                    for user in data_user:
                        if user["lunas"] == "belum":
                            for kamar in data_kamar:
                                if kamar["nomor"] == user["nomor kamar"]:
                                    table.add_row([user["username"], user["nomor kamar"], user["tenggat"], kamar["harga bulanan"]])
                                    ada = True
                    
                    if ada:
                        print(table)
                    else:
                        print("\ngaada yg ngutang\n")
                        

                elif pilihan == '3':
                    table = PrettyTable()
                    table.title = "Orang-orang Penuh Pahala"
                    table.field_names = ["Nama", "Nomor kamar", "Tanggal bayar"]

                    ada = False
                    for user in data_user:
                        if user["lunas"] == "lunas":
                            table.add_row([user["username"], user["nomor kamar"], user["terakhir bayar"]])
                            ada = True
                    
                    if ada:
                        print(table)
                    else:
                        print("\ngaada yg dah bayar\n")

                elif pilihan == '4':
                    menu_admin()
                else:
                    print("Pilihan tidak valid!\n")
        elif pilihan == '4':
            while True:
                print(f"\n{'='*10} Pemasukan {'='*10}")
                print("[1] Pemasukan Tahunan")
                print("[2] Pemasukan Bulanan")
                print("[3] Pemasukan Sepanjang Masa")
                print("[4] Pemasukan Terbanyak")
                print("[5] Kembali")
                pilihan = inputhandler("Pilihan: ")
                if pilihan == '1':
                    print(f"\n{'='*10} Pemasukan Tahunan {'='*10}")
                    pemasukan = 0
                    for data in data_pemasukan:
                        if data["tahun"] == tahun:
                            pemasukan += data["pemasukan"]
                    print(f"pemasukan tahun nie: {format_uang(pemasukan)}\n")
                    while True:
                        print("[1] Cari")
                        print("[2] Kembali")
                        pilihan = inputhandler("Pilihan: ")
                        if pilihan == '1':
                            cari = inputhandler("Tahun: ")
                            pemasukan = 0
                            ada =  False
                            for data in data_pemasukan:
                                if data["tahun"] == cari:
                                    pemasukan += data["pemasukan"]
                                    ada = True
                            if ada:
                                print(f"pemasukan tahun {cari}: {format_uang(pemasukan)}\n")
                            else:
                                print("Data tidak tersedia\n")
                        elif pilihan == '2':
                            break
                elif pilihan == '2':
                    print(f"\n{'='*10} Pemasukan Bulanan {'='*10}")
                    for data in data_pemasukan:
                        if data["tahun"] == tahun and data["bulan"] == bulan:
                            pemasukan = data["pemasukan"]
                            print(f"pemasukan bulan nie: {format_uang(pemasukan)}")
                            while True:
                                print("[1] Cari")
                                print("[2] Kembali")
                                pilihan = inputhandler("Pilihan: ")
                                if pilihan == '1':
                                    ada = False
                                    while True:
                                        tgl = inputhandler("bulan/tahun: ").split('/')
                                        if len(tgl) < 2:
                                            print("Format input tidak valid. Contoh input yang benar: 11/2023\n")
                                        else:
                                            break
                                    for data in data_pemasukan:
                                        if data["tahun"] == tgl[1] and data["bulan"] == tgl[0]:
                                            pemasukan = data["pemasukan"]
                                            ada = True
                                    if ada:
                                        print(f"\npemasukan {tgl[0]}/{tgl[1]}: {format_uang(pemasukan)}")
                                    else:
                                        print("Data tidak tersedia\n")
                                elif pilihan == '2':
                                    break
                elif pilihan == '3':
                    print(f"\n{'='*10} Pemasukan Total {'='*10}")
                    pemasukan = 0
                    for data in data_pemasukan:
                        pemasukan += data["pemasukan"]
                    print(f"pemasukan: {format_uang(pemasukan)}")
                elif pilihan == '4':
                    print(f"\n{'='*10} Pemasukan Terbanyak {'='*10}")
                    pemasukan_tahunan = {}
                    for data in data_pemasukan:
                        pemasukan = data["pemasukan"]

                        # jika data["tahun"] ada di dalam dict pemasukan_tahunan sebagai key
                        if data["tahun"] in pemasukan_tahunan:
                            pemasukan_tahunan[data["tahun"]] += pemasukan
                        else:
                            pemasukan_tahunan[data["tahun"]] = pemasukan

                    # jika dict pemasukan_tahunan tidak kosong
                    if pemasukan_tahunan:
                        # max = value terbesar dari list (bisa juga dari dict)
                        # disini aku pakai dict, agak bingung jelasinnya
                        tahun_tertinggi = max(pemasukan_tahunan, key=pemasukan_tahunan.get)
                        pemasukan_tertinggi = pemasukan_tahunan[tahun_tertinggi]
                        print(f"Tahun dengan pemasukan tertinggi adalah {tahun_tertinggi}: {format_uang(pemasukan_tertinggi)}")
                    else:
                        print("Tidak ada data pemasukan yang tersedia.")
                    
                    pemasukan_bulanan = {}
                    for data in data_pemasukan:
                        key = f"{data['bulan']}/{data['tahun']}"
                        if key in pemasukan_bulanan:
                            pemasukan_bulanan[key] += data['pemasukan']
                        else:
                            pemasukan_bulanan[key] = data['pemasukan']
                    if pemasukan_bulanan:
                        bulan_tertinggi = max(pemasukan_bulanan, key=pemasukan_bulanan.get)
                        pemasukan_tertinggi = pemasukan_bulanan[bulan_tertinggi]
                        print(f"Bulan dengan pemasukan tertinggi adalah {bulan_tertinggi}: {format_uang(pemasukan_tertinggi)}")
                    else:
                        print("Tidak ada data pemasukan yang tersedia.")
                elif pilihan == '5':
                    menu_admin()
                    break
        elif pilihan == '5':
            print(f"\n{'='*10} Pengaturan Akun Admin {'='*10}")
            while True:
                print("[1] Ganti username")
                print("[2] Ganti password")
                print("[3] Kembali")
                pilihan = inputhandler("Pilihan: ")
                if pilihan == '1':
                    while True:
                        username_baru = inputhandler("Username baru: ").strip()
                        if len(username_baru) < 5:
                            print("kependekan, minimal 5 hurup lah")
                        else:
                            break
                    konfirmasi = inputhandler("Apakah anda yakin? [y/n]: ")
                    # lower tu untuk bikin huruf besar jadi kecil.
                    if konfirmasi.lower() == 'y':
                        adminpass["username"] = username_baru
                        simpan_data()
                        print(f"\nUsername anda telah diubah ke {username_baru}")
                        break
                    else:
                        print("Berhasil dibatalkan")

                elif pilihan == '2':
                    while True:
                        password_baru = pwinput.pwinput("Password baru: ", mask='*').strip()
                        if len(password_baru) < 5:
                            print("kependekan, minimal 5 hurup lah")
                        else:
                            break
                    konfirmasi = inputhandler("Apakah anda yakin? [y/n]: ")
                    if konfirmasi.lower() == 'y':
                        adminpass["password"] = password_baru
                        simpan_data()
                        print(f"\nPassword anda telah diubah")
                        break
                    else:
                        print("\nBerhasil dibatalkan")
                elif pilihan == '3':
                    break
                else:
                    print("Pilihan tidak valid!\n")
        elif pilihan == '6':
            menu_awal()
        else:
            print("Pilihan tidak valid!\n")

def login_admin():
    print(f"\n{'='*10} admin mw lewat {'='*10}")
    username = inputhandler("Username: ")
    password = pwinput.pwinput("Password: ", mask='*')

    sukses = False
    if adminpass["username"] == username and adminpass["password"] == password:
            sukses = True
    
    if sukses:
        global user_type
        user_type = "admin"
        print("\nlari ada admin")
        
        refresh_table_kamar()
        menu_admin()
    else:
        print("\ngagal")
#-------------------------------------#



#-------------user normal-------------#
def pesan_kamar():
    print(tabel_kamar)
    pilihan = inputhandler("Pilih nomor: ")
    kamar_ada = False
    if current_user["nomor kamar"] != "NA":
        print(f"Anda sudah memiliki kamar ('{current_user['nomor kamar']}')")
    else:
        for kamar in data_kamar:
            if kamar["nomor"] == pilihan:
                kamar_ada = True
                if kamar["pemilik"] == '':
                    if current_user["saldo"] >= kamar["harga bulanan"]:
                        
                        current_user["terakhir bayar"] = tanggal
                        current_user["lunas"] = "lunas"
                        current_user["nomor kamar"] = pilihan
                        current_user["tenggat"] = (today + timedelta(days=30)).strftime("%d/%m/%Y %H:%M")
                        kamar["pemilik"] = current_user["username"]
                        
                        for data in data_pemasukan:
                            if data["tahun"] == tahun and data["bulan"] == bulan:
                                data["pemasukan"] += kamar["harga bulanan"]
                                break
                        else:
                            data_pemasukan.append({"tahun": tahun, "bulan": bulan, "pemasukan": kamar["harga bulanan"]})

                        sisa_duid = current_user["saldo"] - kamar["harga bulanan"]
                        invoice = PrettyTable()
                        invoice.title = "Detail Pemesanan"
                        invoice.field_names = ["Nomor", "Waktu Pemesanan", "Berlaku Hingga", "Harga Bulanan"]
                        invoice.add_rows([
                            [kamar["nomor"], tanggal, current_user["tenggat"], format_uang(kamar["harga bulanan"])],
                            ['','','-'*10,'-'*10],
                            ['','',"Saldo:", format_uang(current_user["saldo"])],
                            ['','',"sisa duid:", format_uang(sisa_duid)]
                        ])
                        current_user["saldo"] = sisa_duid
                        global kamar_user
                        kamar_user = kamar
                        simpan_data()

                        print(invoice)
                        refresh_table_kamar()
                        return
                    elif current_user["saldo"] == 0:
                        print("Anda tidak memiliki uang, mohon isi saldo anda\n")
                        return
                    else:
                        print(f"Anda hanya memiliki {format_uang(current_user['saldo'])}, mohon isi saldo anda\n")
                else:
                    print("udah ada yang punya\n")
                    return
        if not kamar_ada:
            print("gaada kamar itu\n")
            return

def bayar(bulan_dibayar):
    if current_user["saldo"] >= kamar_user["harga bulanan"]:
        current_user["terakhir bayar"] = tanggal
        parsed_tenggat = datetime.strptime(current_user["tenggat"], "%d/%m/%Y %H:%M")

        if bulan_dibayar == 2:
            current_user["tenggat"] = (parsed_tenggat+timedelta(days=60)).strftime("%d/%m/%Y %H:%M")
            current_user["lunas"] = "lunas"
        else:
            if str(parsed_tenggat.strftime("%m/%Y")) == f"{int(bulan)+1}/{tahun}":
                current_user["lunas"] = "lunas"
            else:
                current_user["tenggat"] = (parsed_tenggat+timedelta(days=30)).strftime("%d/%m/%Y %H:%M")
        
        for data in data_pemasukan:
            if data["tahun"] == tahun and data["bulan"] == bulan:
                data["pemasukan"] += kamar_user["harga bulanan"]*bulan_dibayar
                break
        else:
            data_pemasukan.append({"tahun":tahun, "bulan":bulan, "pemasukan":kamar_user["harga bulanan"]*bulan_dibayar})
        
        sisa_duid = current_user["saldo"] - kamar_user["harga bulanan"]*bulan_dibayar
        invoice = PrettyTable()
        invoice.title = "Detail Pembayaran"
        invoice.field_names = ["Nomor", "Waktu Pembayaran", "Berlaku Hingga", "Bulan", "Harga Bulanan"]
        invoice.add_rows([
            [kamar_user["nomor"], tanggal, current_user["tenggat"], bulan_dibayar, format_uang(kamar_user["harga bulanan"])],
            ['','','','-'*10,'-'*10],
            ['','','',"Saldo:", format_uang(current_user["saldo"])],
            ['','','',"sisa duid:", format_uang(sisa_duid)]
        ])
        current_user["saldo"] = sisa_duid
        simpan_data()
        print(invoice)
    elif current_user["saldo"] == 0:
        print("Anda tidak memiliki uang, mohon isi saldo anda\n")
    else:
        print(f"Anda hanya memiliki {format_uang(current_user['saldo'])}, mohon isi saldo anda\n")

def setting_user():
    print(f"\n{'='*10} Pengaturan Akun {'='*10}")
    while True:
        print("[1] Ganti username")
        print("[2] Ganti password")
        print("[3] Kembali")
        pilihan = inputhandler("Pilihan: ")
        if pilihan == '1':
            while True:
                username_baru = inputhandler("Username baru: ").strip()
                if len(username_baru) < 5:
                    print("kependekan, minimal 5 hurup lah")
                else:
                    break
            konfirmasi = inputhandler("Apakah anda yakin? [y/n]: ")
            # lower tu untuk bikin huruf besar jadi kecil.
            if konfirmasi.lower() == 'y':
                for user in userpass:
                    if user["username"] == current_user["username"]:
                        current_user["username"] = username_baru
                        user["username"] = username_baru
                        if current_user["nomor kamar"] != "NA":
                            kamar_user["pemilik"] = username_baru

                simpan_data()
                refresh_table_kamar()
                print(f"\nUsername anda telah diubah ke {username_baru}")
                lihat_akun(current_user["username"])
                break
            else:
                print("Berhasil dibatalkan")

        elif pilihan == '2':
            while True:
                password_baru = pwinput.pwinput("Password baru: ", mask='*').strip()
                if len(password_baru) < 5:
                    print("kependekan, minimal 5 hurup lah")
                else:
                    break
            konfirmasi = inputhandler("Apakah anda yakin? [y/n]: ")
            if konfirmasi.lower() == 'y':
                for user in userpass:
                    if user["username"] == current_user["username"]:
                        user["password"] = password_baru
                        simpan_data()
                        print(f"\nPassword anda telah diubah")
                        lihat_akun(current_user["username"])
                        break
            else:
                print("\nBerhasil dibatalkan")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!\n")

def ket(hari):
    if hari == 0:
        keterangan = "Hari ini"
    elif hari < 0:
        keterangan = f"{-hari} hari yang lalu"
    else:
        keterangan = f"{hari} hari lagi"
    return keterangan

def lihat_akun(username):
    print(f"\n{'='*10} Akun {'='*10}")
    for user in data_user:
        if user["username"] == username:
            print(f"Username: {user['username']}")
            print(f"Saldo: {format_uang(user['saldo'])}")

            if user["nomor kamar"] == "NA":
                print("belom punya kamar")
                if user_type != "admin":
                    while True:
                        print("[1] Pengaturan Akun")
                        print("[2] Kembali")
                        pilihan = inputhandler("Pilihan: ")
                        if pilihan == '1':
                            setting_user()
                            break
                        elif pilihan == '2':
                            menu_user()
                            break
                        else:
                            print("Pilihan tidak valid!\n")
            else:
                for kamar in data_kamar:
                    if kamar["nomor"] == user["nomor kamar"]:
                        # strptime = string parse time (ubah string tanggal menjadi objek datetime)
                        tenggat = datetime.strptime(user["tenggat"], "%d/%m/%Y %H:%M")
                        sisa_hari = (tenggat - today).days
                        
                        # terakhir bayar n hari yg lalu
                        tb = (today - datetime.strptime(user['terakhir bayar'], "%d/%m/%Y %H:%M")).days
                        
                        print(f"Nomor Kamar: {user['nomor kamar']}")
                        print(f"Terakhir Bayar: {user['terakhir bayar']} ({ket(-tb)})")
                        if kamar_user["ketersediaan"] == "pending":
                            print("Peringatan: Kamar anda akan dihapus, segera keluar plis\n")
                            
                        if user["lunas"] == "lunas":
                            print(f"Berlaku hingga: {user['tenggat']} ({ket(sisa_hari)})")
                            print("Lunas\n")
                            if user_type != "admin":
                                while True:
                                    print("[1] Pengaturan Akun")
                                    print("[2] Kembali")
                                    pilihan = inputhandler("Pilihan: ")
                                    if pilihan == '1':
                                        setting_user()
                                        break
                                    elif pilihan == '2':
                                        menu_user()
                                        break
                                    else:
                                        print("Pilihan tidak valid!\n")
                        else:
                            print(f"Tenggat: {user['tenggat']} ({ket(sisa_hari)})")
                            bulan_nunggak = 1
                            if today > tenggat:
                                bulan_nunggak = 2
                                print("Belum bayar bulan lalu")
                                print(f"Sisa {5 + sisa_hari} hari lagi sebelum kamar loe hilang")
                            print(f"Tagihan: {format_uang(kamar['harga bulanan']*bulan_nunggak)}\n")
                            
                            # buat ngilangin tombol bayar kalo yg login itu admin
                            if user_type != 'admin':
                                while True:
                                    print("[1] Pengaturan Akun")
                                    print("[2] Bayar")
                                    print("[3] Kembali")
                                    pilihan = inputhandler("Pilihan: ")
                                    if pilihan == '1':
                                        setting_user()
                                    elif pilihan == '2':
                                        if bulan_nunggak > 1:
                                            print("[1] Bayar 1 bulan")
                                            print("[2] Langsung lunas")
                                            print("[3] Kembali")
                                            pilihan = inputhandler("Pilihan: ")
                                            if pilihan == '1':
                                                bayar(1)
                                            elif pilihan == '2':
                                                bayar(2)
                                            elif pilihan== '3':
                                                return
                                            else:
                                                print("Pilihan tidak valid!\n")
                                        else:
                                            bayar(1)
                                    elif pilihan == '3':
                                        menu_user()
                                        return
                                    else:
                                        print("Pilihan tidak valid!\n")
                        return
            return
    print("akun gak ketemu\n")

def tambah_saldo():
        while True:
            duit = inputhandler("brp bos?: ", "int")
            if duit > 0:
                current_user["saldo"] += duit
                simpan_data()
                print(f"{format_uang(duit)} berhasil ditambah ke saldo anda\n")
                break
            else:
                print("\ngabisa negatif ye")

def berhenti():
    if current_user["nomor kamar"] != "NA":
        if current_user["lunas"] == "lunas":
            konfirmasi = inputhandler(f"Apakah anda yakin ingin berhenti menyewa kamar {current_user['nomor kamar']}? [y/n]: ")
            if konfirmasi.lower() == 'y':
                print(f"\nAnda telah berhenti tinggal di kamar {current_user['nomor kamar']}")
                kamar_user["pemilik"] = ''
                current_user["nomor kamar"] = "NA"
                current_user["tenggat"] = "NA"
                if kamar_user["ketersediaan"] == "pending":
                    data_kamar.remove(kamar_user)
                else:
                    kamar_user["ketersediaan"] == "tersedia"
                simpan_data()
                refresh_table_kamar()
            else:
                print("\nBerhasil dibatalkan.")
        else:
            print("bayar utang dulu\n")
    else:
        print("nyewa aja nggak\n")

def menu_user():
    print(f"\n{'='*10} Menu Utama {'='*10}")
    while True:
        print("[1] Pesan kamar")
        print("[2] Lihat akun")
        print("[3] Tambah saldo")
        print("[4] Berhenti menyewa")
        print("[5] Keluar")
        pilihan = inputhandler("Pilihan: ")
        if pilihan == '1':
            pesan_kamar()
        elif pilihan == '2':
            lihat_akun(current_user["username"])
        elif pilihan == '3':
            tambah_saldo()
        elif pilihan == '4':
            berhenti()
        elif pilihan == '5':
            menu_awal()
        else:
            print("Pilihan tidak valid!\n")

def menu_register():
    print(f"\n{'='*10} Registrasi Akun {'='*10}")
    while True:
        username = inputhandler("Username: ").strip()
        if len(username) < 5:
            print("kependekan, minimal 5 hurup lah")
        else:
            break
    while True:
        try:
            password = pwinput.pwinput("Password: ", mask='*').strip()
            if len(password) < 5:
                print("kependekan, minimal 5 hurup lah")
            else:
                break
        except KeyboardInterrupt:
            print("ea")

    sudah_ada = False
    for akun in userpass:
        if akun["username"] == username:
            sudah_ada = True
    
    if sudah_ada:
        print("username udah ada")
    else:
        data_user.append({"username": username, "nomor kamar": "NA", "terakhir bayar": "NA", "tenggat": "NA", "lunas": "belum", "saldo": 0})
        simpan_data()

        userpass.append({"username": username, "password": password})
        with open('userpass.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([username, password])

        global user_type, current_user
        user_type = "normal"
        current_user = data_user[-1]
        
        print("\nAkun berhasil dibuat")

        refresh_table_kamar()
        menu_user()

def menu_login():
    print(f"\n{'='*10} Login {'='*10}")
    username = inputhandler("Username: ")
    password = pwinput.pwinput("Password: ", mask='*')

    sukses = False
    for akun in userpass:
        if akun["username"] == username and akun["password"] == password:
            sukses = True
    
    if sukses:
        global user_type
        user_type = "normal"
        for user in data_user:
            if user["username"] == username:
                global current_user
                current_user = user
                if user["nomor kamar"] != "NA":
                    for kamar in data_kamar:
                        if kamar["pemilik"] == username:
                            global kamar_user
                            kamar_user = kamar
                    
        print("\nberhasil login")
        
        for user in data_user:
            if user["username"] == current_user["username"] and user["tenggat"] != "NA":
                # string tenggat waktu diubah ke objek datetime
                parsed_tenggat = datetime.strptime(user["tenggat"], "%d/%m/%Y %H:%M")
                # sama, tapi untuk tanggal terakhir bayar
                parsed_tb = datetime.strptime(user["terakhir bayar"], "%d/%m/%Y %H:%M")
                # brp hari lewat dari tenggat
                lewat = (today-parsed_tenggat).days
                if today > parsed_tenggat:
                    user["lunas"] = "belum"
                    if (today - parsed_tb).days < 60:
                        user["tenggat"] = (parsed_tenggat+timedelta(days=30)).strftime("%d/%m/%Y %H:%M")
                        simpan_data()
                    elif lewat > 0 and lewat < 5:
                        print("Cepati bayar!!!!!!!!!")
                    elif lewat >= 5:
                        kamar_user["pemilik"] = ""
                        current_user["nomor kamar"] = "NA"
                        simpan_data()
                        print("Kamar loe hilang, mampus")

        refresh_table_kamar()
        menu_user()
    else:
        print("gagal")
#------------------------------#



def menu_awal():
    print('='*10, "Pilih Role", '='*10)
    while True:
        print("[1] Pengunjung")
        print("[2] Admin")
        print("[3] Matiin")
        while True:
            try:
                pilihan = inputhandler("Pilih: ")
                break
            except KeyboardInterrupt:
                print("ea\n")
        if pilihan == '1':
            pilihan = inputhandler("Apakah anda sudah memiliki akun? [y/n]: ")
            if pilihan.lower() == 'y':
                menu_login()
            elif pilihan.lower() == 'n':
                menu_register()
        elif pilihan == '2':
            login_admin()
        elif pilihan == '3':
            print("\ndadah")
            # exit tu nutup program secara keseluruhan
            exit()
        else:
            print("Pilihan tidak valid!\n")

print('='*7, "Kosan Pembualan", '='*8, '\n')
menu_awal()