import os
from prettytable import PrettyTable

# Definisikan kelas Perhiasan untuk merepresentasikan setiap item perhiasan
class Perhiasan:
    def __init__(self, id_barang, nama, material, harga, stok, berat):
        self.id_barang = id_barang
        self.nama = nama
        self.material = material
        self.harga = harga
        self.stok = stok
        self.berat = berat

# Definisikan kelas Node untuk LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definisikan kelas LinkedList untuk menyimpan barang-barang perhiasan
class LinkedList:
    def __init__(self):
        self.head = None

    # Tambahkan node baru di awal linked list
    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Tambahkan node baru di akhir linked list
    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Tambahkan node baru setelah node tertentu
    def tambah_di_antara(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Hapus node pertama dari linked list
    def hapus_di_awal(self):
        if not self.head:
            print("LinkedList kosong.")
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    # Hapus node terakhir dari linked list
    def hapus_di_akhir(self):
        if not self.head:
            print("LinkedList kosong.")
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Hapus node setelah node tertentu
    def hapus_di_antara(self, prev_node):
        if not prev_node or not prev_node.next:
            print("Node tidak ditemukan.")
            return
        temp = prev_node.next
        prev_node.next = prev_node.next.next
        temp = None

# Definisikan kelas TokoPerhiasan untuk operasi-operasi pada barang-barang perhiasan
class TokoPerhiasan:
    def __init__(self):
        self.inventaris_perhiasan = LinkedList()

    # Tambahkan perhiasan ke inventaris pada posisi tertentu
    def tambah_perhiasan(self, id_barang, nama, material, harga, stok, berat, posisi="akhir"):
        if posisi == "awal":
            self.inventaris_perhiasan.tambah_di_awal(Perhiasan(id_barang, nama, material, harga, stok, berat))
        elif posisi == "akhir":
            self.inventaris_perhiasan.tambah_di_akhir(Perhiasan(id_barang, nama, material, harga, stok, berat))
        else:
            current = self.inventaris_perhiasan.head
            while current:
                if current.data.id_barang == posisi:
                    self.inventaris_perhiasan.tambah_di_antara(current, Perhiasan(id_barang, nama, material, harga, stok, berat))
                    return
                current = current.next
            print("Posisi tidak ditemukan.")

    # Lihat semua barang dalam inventaris
    def lihat_perhiasan(self):
        if not self.inventaris_perhiasan.head:
            print("Inventaris kosong.")
            return

        table = PrettyTable()
        table.field_names = ["ID Barang", "Nama", "Material", "Harga", "Stok", "Berat"]

        current = self.inventaris_perhiasan.head
        while current:
            table.add_row([current.data.id_barang, current.data.nama, current.data.material, current.data.harga, current.data.stok, current.data.berat])
            current = current.next

        print(table)

    # Perbarui atribut dari barang dalam inventaris berdasarkan ID barang
    def perbarui_perhiasan(self, id_barang):
        if not self.inventaris_perhiasan.head:
            print("Inventaris kosong.")
            return

        current = self.inventaris_perhiasan.head
        while current:
            if current.data.id_barang == id_barang:
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
                    current.data.nama = value
                    print("Nama barang berhasil diperbarui.")
                elif pilihan_atribut == 2:
                    value = input("Masukkan nilai baru untuk Material: ")
                    current.data.material = value
                    print("Material barang berhasil diperbarui.")
                elif pilihan_atribut == 3:
                    value = int(input("Masukkan nilai baru untuk Harga: "))
                    current.data.harga = value
                    print("Harga barang berhasil diperbarui.")
                elif pilihan_atribut == 4:
                    value = int(input("Masukkan nilai baru untuk Stok: "))
                    current.data.stok = value
                    print("Stok barang berhasil diperbarui.")
                elif pilihan_atribut == 5:
                    value = float(input("Masukkan nilai baru untuk Berat (gram): "))
                    current.data.berat = value
                    print("Berat barang berhasil diperbarui.")
                else:
                    print("Atribut yang dimasukkan tidak valid.")
                return
            current = current.next

        print("Tidak ada barang dengan ID tersebut.")

    # Hapus barang dari inventaris berdasarkan ID barang
    def hapus_perhiasan(self, id_barang):
        if not self.inventaris_perhiasan.head:
            print("Inventaris kosong.")
            return

        prev_node = None
        current = self.inventaris_perhiasan.head
        while current:
            if current.data.id_barang == id_barang:
                if prev_node is None:
                    self.inventaris_perhiasan.hapus_di_awal()
                else:
                    self.inventaris_perhiasan.hapus_di_antara(prev_node)
                print("Barang berhasil dihapus.")
                return
            prev_node = current
            current = current.next

        print("Barang tidak ditemukan.")

# Bersihkan layar terminal
os.system("cls")

# Tampilkan header toko
print("+----------------------------------------------+")
print("|         TOKO PERHIASAN HJ SONDANG            |")
print("+----------------------------------------------+")

# Inisialisasi objek TokoPerhiasan
toko = TokoPerhiasan()

# Loop utama program
while True:
    print("==============| SILAHKAN PILIH |===============")
    print("[1] MENAMBAHKAN BARANG                         ")
    print("[2] MELIHAT BARANG                             ")
    print("[3] MEMPERBARUI BARANG                         ")
    print("[4] MENGHAPUS BARANG                           ")
    print("[5] KELUAR                                     ")
    print("===============================================")
    
    # Meminta input pilihan dari pengguna
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))

    # Memproses pilihan pengguna
    if pilihan == 1:
        os.system("cls")
        print("====| POSISI PENAMBAHAN |====")
        print("[1] Awal")
        print("[2] Tengah")
        print("[3] Akhir")
        print("==============================")
        posisi_pilihan = int(input("Masukkan pilihan posisi penambahan (1/2/3): "))
        id_barang = int(input("Masukkan ID barang: "))
        nama = input("Masukkan Nama barang: ")
        material = input("Masukkan Material barang: ")
        harga = int(input("Masukkan Harga barang: "))
        stok = int(input("Masukkan Stok barang: "))
        berat = float(input("Masukkan Berat barang(gram): "))
        if posisi_pilihan == 2:
            posisi = int(input("Masukkan ID barang setelah posisi yang diinginkan: "))
        else:
            posisi = "awal" if posisi_pilihan == 1 else "akhir"
        toko.tambah_perhiasan(id_barang, nama, material, harga, stok, berat, posisi)
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
        print("Terima kasih telah menggunakan program ini. tata titi tutu")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-5.")