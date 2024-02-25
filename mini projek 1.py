import os
from prettytable import PrettyTable

class Perhiasan:
    def __init__(self, id_barang, nama, material, harga, stok, berat):
        self.id_barang = id_barang
        self.nama = nama
        self.material = material
        self.harga = harga
        self.stok = stok
        self.berat = berat

class TokoPerhiasan:
    def __init__(self):
        self.inventaris_perhiasan = {}

    def tambah_perhiasan(self, id_barang, nama, material, harga, stok, berat):
        if id_barang not in self.inventaris_perhiasan:
            self.inventaris_perhiasan[id_barang] = Perhiasan(id_barang, nama, material, harga, stok, berat)
            print("Barang berhasil ditambahkan.")
        else:
            print("ID barang sudah ada.")

    def lihat_perhiasan(self):
        if self.inventaris_perhiasan:
            table = PrettyTable()
            table.field_names = ["ID Barang", "Nama", "Material", "Harga", "Stok", "Berat"]
            for barang in self.inventaris_perhiasan.values():
                table.add_row([barang.id_barang, barang.nama, barang.material, barang.harga, barang.stok, barang.berat])
            print(table)
        else:
            print("Inventaris kosong.")
    
    def perbarui_perhiasan(self, id_barang):
        if id_barang in self.inventaris_perhiasan:
            barang = self.inventaris_perhiasan[id_barang]

            print("===| Atribut yang ingin diperbarui |===")
            print("1. Nama")
            print("2. Material")
            print("3. Harga")
            print("4. Stok")
            print("5. Berat")
            print("=======================================")
            pilihan_atribut = int(input("Pilih atribut yang ingin diperbarui (1/2/3/4/5): "))
            
            if pilihan_atribut == 1:
                value = input("Masukkan nilai baru untuk Nama: ")
                barang.nama = value
                print("Nama barang berhasil diperbarui.")
            elif pilihan_atribut == 2:
                value = input("Masukkan nilai baru untuk Material: ")
                barang.material = value
                print("Material barang berhasil diperbarui.")
            elif pilihan_atribut == 3:
                value = int(input("Masukkan nilai baru untuk Harga: "))
                barang.harga = value
                print("Harga barang berhasil diperbarui.")
            elif pilihan_atribut == 4:
                value = int(input("Masukkan nilai baru untuk Stok: "))
                barang.stok = value
                print("Stok barang berhasil diperbarui.")
            elif pilihan_atribut == 5:
                value = float(input("Masukkan nilai baru untuk Berat (gram): "))
                barang.berat = value
                print("Berat barang berhasil diperbarui.")
            else:
                print("Atribut yang dimasukkan tidak valid.")
        else:
            print("Tidak ada barang dengan ID tersebut.")
    
    def hapus_perhiasan(self, id_barang):
        if id_barang in self.inventaris_perhiasan:
            del self.inventaris_perhiasan[id_barang]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")

os.system("cls")
print("+----------------------------------------------+")
print("|         TOKO PERHIASAN HJ SONDANG            |")
print("+----------------------------------------------+")
toko = TokoPerhiasan()
while True:
    print("==============| SILAHKAN PILIH |===============")
    print("[1] MENAMBAHKAN BARANG                         ")
    print("[2] MELIHAT BARANG                             ")
    print("[3] MEMPERBARUI BARANG                         ")
    print("[4] MENGHAPUS BARANG                           ")
    print("[5] KELUAR                                     ")
    print("===============================================")
    
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))
    if pilihan == 1:
        os.system("cls")
        id_barang = int(input("Masukkan ID barang: "))
        nama = input("Masukkan Nama barang: ")
        material = input("Masukkan Material barang: ")
        harga = int(input("Masukkan Harga barang: "))
        stok = int(input("Masukkan Stok barang: "))
        berat = float(input("Masukkan Berat barang(gram): "))
        toko.tambah_perhiasan(id_barang, nama, material, harga, stok, berat)
    elif pilihan == 2:
        toko.lihat_perhiasan()
    elif pilihan == 3:
        os.system("cls")
        id_barang = int(input("Masukkan ID barang yang ingin diperbarui: "))
        toko.perbarui_perhiasan(id_barang)
    elif pilihan == 4:
        os.system("cls")
        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
        toko.hapus_perhiasan(id_barang)
    elif pilihan == 5:
        os.system("cls")
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-5.")
