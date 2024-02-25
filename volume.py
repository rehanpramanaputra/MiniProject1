import math

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def hitung_volume_prisma_segitiga(alas, tinggi_prisma):
    volume = 0.5 * alas * tinggi_prisma
    return volume

def hitung_volume_bola(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def main():
    print("Pilih bentuk bangun:")
    print("1. Balok")
    print("2. Prisma Segitiga")
    print("3. Bola")
    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    if pilihan == 1:
        print("Masukkan panjang, lebar, dan tinggi balok:")
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar: "))
        tinggi = float(input("Tinggi: "))
        volume = hitung_volume_balok(panjang, lebar, tinggi)
        print("Volume balok adalah:", volume)
    elif pilihan == 2:
        print("Masukkan alas segitiga dan tinggi prisma:")
        alas = float(input("Alas segitiga: "))
        tinggi_prisma = float(input("Tinggi prisma: "))
        volume = hitung_volume_prisma_segitiga(alas, tinggi_prisma)
        print("Volume prisma segitiga adalah:", volume)
    elif pilihan == 3:
        radius = float(input("Masukkan jari-jari bola: "))
        volume = hitung_volume_bola(radius)
        print("Volume bola adalah:", volume)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
