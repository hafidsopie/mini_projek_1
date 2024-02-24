import os
from prettytable import PrettyTable

class TokoPerhiasan:
    def __init__(self):
        self.inventaris_perhiasan = {}

    def tambah_perhiasan(self, id_barang, nama, material, harga, stok, berat):
        if id_barang not in self.inventaris_perhiasan:
            self.inventaris_perhiasan[id_barang] = {
                'nama': nama,
                'material': material,
                'harga': harga,
                'stok': stok,
                'berat': berat
            }
            print("Barang berhasil ditambahkan.")
        else:
            print("ID barang sudah ada.")

    def lihat_perhiasan(self):
        if self.inventaris_perhiasan:
            table = PrettyTable()
            table.field_names = ["ID Barang", "Nama", "Material", "Harga", "Stok", "Berat"]
            for id_barang, barang in self.inventaris_perhiasan.items():
                table.add_row([id_barang, barang['nama'], barang['material'], barang['harga'], barang['stok'], barang['berat']])
            print(table)
        else:
            print("Inventaris kosong.")

    def perbarui_perhiasan(self, id_barang, nama=None, material=None, harga=None, stok=None, berat=None):
        if id_barang in self.inventaris_perhiasan:
            barang = self.inventaris_perhiasan[id_barang]
            if nama is not None:
                barang['nama'] = nama
                print("Nama barang berhasil diperbarui.")
            if material is not None:
                barang['material'] = material
                print("Material barang berhasil diperbarui.")
            if harga is not None:
                barang['harga'] = harga
                print("Harga barang berhasil diperbarui.")
            if stok is not None:
                barang['stok'] = stok
                print("Stok barang berhasil diperbarui.")
            if berat is not None:
                barang['berat'] = berat
                print("Berat barang berhasil diperbarui.")
        else:
            print("Barang tidak ditemukan.")

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
        id_barang = int(input("Masukkan ID barang yang ingin diperbarui: "))
        nama_baru = input("Masukkan nama barang baru: ")
        material_baru = input("Masukkan material baru: ")
        harga_baru = int(input("Masukkan harga baru: "))
        stok_baru = int(input("Masukkan stok baru: "))
        berat_baru = float(input("Masukkan berat baru(gram): "))
        toko.perbarui_perhiasan(id_barang, nama=nama_baru, material=material_baru, harga=harga_baru, stok=stok_baru, berat=berat_baru)
    elif pilihan == 4:
        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
        toko.hapus_perhiasan(id_barang)
    elif pilihan == 5:
        print("Terima kasih telah menggunakan program ini. tata titi tutu :)")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-6.")
