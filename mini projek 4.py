# Import modul os dan PrettyTable
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

    # Metode tambah_di_awal untuk menambahkan node baru di awal linked list
    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Metode tambah_di_akhir untuk menambahkan node baru di akhir linked list
    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Metode tambah_di_antara untuk menambahkan node baru setelah node tertentu
    def tambah_di_antara(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Metode hapus_di_awal untuk menghapus node pertama dari linked list
    def hapus_di_awal(self):
        if not self.head:
            print("LinkedList kosong.")
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    # Metode hapus_di_akhir untuk menghapus node terakhir dari linked list
    def hapus_di_akhir(self):
        if not self.head:
            print("LinkedList kosong.")
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Metode hapus_di_antara untuk menghapus node setelah node tertentu
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

    # Metode tambah_perhiasan untuk menambahkan perhiasan ke inventaris pada posisi tertentu
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

    # Metode lihat_perhiasan untuk melihat semua barang dalam inventaris
    def lihat_perhiasan(self):
        print("+----------------------------------------------------------------+")
        print("|                 DAFTAR PERIHASAN DI TOKO                       |")
        print("+----------------------------------------------------------------+")
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

    # Metode perbarui_perhiasan untuk memperbarui atribut dari barang dalam inventaris berdasarkan ID barang
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

    # Metode hapus_perhiasan untuk menghapus barang dari inventaris berdasarkan ID barang
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

    # Metode quick_sort untuk melakukan sorting menggunakan algoritma quick sort
    def quick_sort(self, arr, attribute1, attribute2, ascending=True):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if getattr(x.data, attribute1) < getattr(pivot.data, attribute1)]
            greater_than_pivot = [x for x in arr[1:] if getattr(x.data, attribute1) > getattr(pivot.data, attribute1)]
            if ascending:
                return self.quick_sort(less_than_pivot, attribute1, attribute2, ascending) + [pivot] + self.quick_sort(greater_than_pivot, attribute1, attribute2, ascending)
            else:
                return self.quick_sort(greater_than_pivot, attribute1, attribute2, ascending) + [pivot] + self.quick_sort(less_than_pivot, attribute1, attribute2, ascending)

    # Metode sort_perhiasan untuk melakukan sorting barang dalam inventaris
    def sort_perhiasan(self, attribute1, attribute2=None, ascending=True):
        if not self.inventaris_perhiasan.head:
            print("Inventaris kosong.")
            return

        # Memeriksa apakah atribut pertama yang diminta adalah ID Barang atau Nama Barang
        if attribute1 != "id_barang" and attribute1 != "nama":
            print("Sortir hanya bisa dilakukan berdasarkan ID Barang atau Nama Barang.")
            return

        # Jika atribut kedua dimasukkan, pastikan itu adalah Nama Barang
        if attribute2 and attribute2 != "nama":
            print("Sortir hanya bisa dilakukan berdasarkan ID Barang atau Nama Barang.")
            return

        arr = []
        current = self.inventaris_perhiasan.head
        while current:
            arr.append(current)
            current = current.next

        # Fungsi untuk membandingkan dua barang berdasarkan atribut yang diberikan
        def compare(x):
            if attribute1 == "id_barang":
                return x.data.id_barang
            elif attribute1 == "nama":
                return x.data.nama

        # Melakukan sortir menggunakan fungsi compare
        sorted_arr = sorted(arr, key=compare, reverse=not ascending)
        self.inventaris_perhiasan.head = sorted_arr[0]
        current = self.inventaris_perhiasan.head
        for node in sorted_arr[1:]:
            current.next = node
            current = current.next
        current.next = None

    # Metode fibonacci_search untuk melakukan pencarian menggunakan algoritma Fibonacci Search
    def fibonacci_search(self, arr, x, attribute):
        low = 0
        high = len(arr) - 1
        fibM_minus_2 = 0
        fibM_minus_1 = 1
        fibM = fibM_minus_1 + fibM_minus_2

        while fibM < len(arr):
            fibM_minus_2 = fibM_minus_1
            fibM_minus_1 = fibM
            fibM = fibM_minus_1 + fibM_minus_2

        offset = -1

        while fibM > 1:
            i = min(offset + fibM_minus_2, len(arr) - 1)

            if getattr(arr[i].data, attribute) < x:
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                offset = i
            elif getattr(arr[i].data, attribute) > x:
                fibM = fibM_minus_2
                fibM_minus_1 -= fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else:
                return i

        if fibM_minus_1 and offset < len(arr) - 1 and getattr(arr[offset + 1].data, attribute) == x:
            return offset + 1

        return -1

    # Metode cari_perhiasan untuk melakukan pencarian barang berdasarkan ID atau Nama
    def cari_perhiasan(self, keyword, attribute):
        if not self.inventaris_perhiasan.head:
            print("Inventaris kosong.")
            return

        keyword = keyword.lower()  # Ubah keyword ke lowercase untuk pencarian case-insensitive

        arr = []
        current = self.inventaris_perhiasan.head
        while current:
            arr.append(current)
            current = current.next

        if attribute == "id_barang":
            keyword = int(keyword)

        found = False  # Menandai apakah setidaknya satu barang ditemukan

        for node in arr:
            if attribute == "id_barang":
                if node.data.id_barang == keyword:
                    print("+----------------------------------------------+")
                    print("|               HASIL PENCARIAN                |")
                    print("+----------------------------------------------+")
                    print("Barang ditemukan:")
                    print("ID Barang:", node.data.id_barang)
                    print("Nama:", node.data.nama)
                    print("Material:", node.data.material)
                    print("Harga:", node.data.harga)
                    print("Stok:", node.data.stok)
                    print("Berat:", node.data.berat)
                    found = True
                    break
            elif attribute == "nama":
                if keyword in node.data.nama.lower(): 
                    if not found:
                        print("Hasil Pencarian:")
                    print("+----------------------------------------------+")
                    print("|               HASIL PENCARIAN                |")
                    print("+----------------------------------------------+")
                    print("ID Barang:", node.data.id_barang)
                    print("Nama:", node.data.nama)
                    print("Material:", node.data.material)
                    print("Harga:", node.data.harga)
                    print("Stok:", node.data.stok)
                    print("Berat:", node.data.berat)
                    found = True

        if not found:
            print("Barang tidak ditemukan.")


# Bersihkan layar terminal
os.system("cls")

# Tampilkan tema toko
print("+----------------------------------------------+")
print("|         TOKO PERHIASAN HJ SONDANG            |")
print("+----------------------------------------------+")

# TokoPerhiasan
toko = TokoPerhiasan()

# Tambahkan beberapa barang ke dalam inventaris
toko.tambah_perhiasan(1, "Cincin ", "Emas", 5000000, 10, 5.2)
toko.tambah_perhiasan(2, "Kalung ", "Perak", 3500000, 15, 8.7)
toko.tambah_perhiasan(3, "Anting-anting ", "Emas", 2000000, 20, 2.5)
toko.tambah_perhiasan(4, "Gelang ", "Perak", 4500000, 8, 6.1)
toko.tambah_perhiasan(5, "Liontin", "Emas", 6000000, 12, 4.8)

# Menu utama program
while True:
    print("==============| SILAHKAN PILIH |===============")
    print("[1] MENAMBAHKAN BARANG                         ")
    print("[2] MELIHAT BARANG                             ")
    print("[3] MEMPERBARUI BARANG                         ")
    print("[4] MENGHAPUS BARANG                           ")
    print("[5] SORTIR BARANG                              ")
    print("[6] CARI BARANG                                ")
    print("[7] KELUAR                                     ")
    print("===============================================")

    # Input pilihan dari pengguna
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6/7): "))

    # Memproses pilihan pengguna
    if pilihan == 1:
        os.system("cls")
        print("+----------------------------------------------+")
        print("|        MENAMBAHKAN PERIHASAN DI TOKO         |")
        print("+----------------------------------------------+")
        print("==========|   POSISI  PENAMBAHAN   |===========")
        print("[1] Awal")
        print("[2] Tengah")
        print("[3] Akhir")
        print("===============================================")
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
        print("+----------------------------------------------+")
        print("|        MEMPERBARUI PERIHASAN DI TOKO         |")
        print("+----------------------------------------------+")
        id_barang = int(input("Masukkan ID barang yang ingin diperbarui: "))
        toko.perbarui_perhiasan(id_barang)
    elif pilihan == 4:
        os.system("cls")
        print("+----------------------------------------------+")
        print("|         MENGHAPUS PERIHASAN DI TOKO          |")
        print("+----------------------------------------------+")
        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
        toko.hapus_perhiasan(id_barang)
    elif pilihan == 5:
        os.system("cls")
        print("====| PILIH KRITERIA SORTIR |====")
        print("[1] Ascending (A -> Z)")
        print("[2] Descending (Z -> A)")
        print("==================================")
        sort_pilihan = int(input("Masukkan pilihan kriteria sortir (1/2): "))
        print("====| PILIH KRITERIA URUTAN |====")
        print("[1] ID Barang")
        print("[2] Nama Barang")
        print("==================================")
        urutan_pilihan = int(input("Masukkan pilihan kriteria urutan (1/2): "))
        attribute1 = ""
        attribute2 = None
        if urutan_pilihan == 1:
            attribute1 = "id_barang"
        elif urutan_pilihan == 2:
            attribute1 = "nama"
        ascending = sort_pilihan == 1
        toko.sort_perhiasan(attribute1, attribute2, ascending)
    elif pilihan == 6:
        os.system("cls")
        print("====| PILIH KRITERIA PENCARIAN |====")
        print("[1] Cari berdasarkan ID Barang")
        print("[2] Cari berdasarkan Nama Barang")
        print("====================================")
        search_pilihan = int(input("Masukkan pilihan kriteria pencarian (1/2): "))
        keyword = input("Masukkan kata kunci pencarian: ")
        attribute = "id_barang" if search_pilihan == 1 else "nama"
        toko.cari_perhiasan(keyword, attribute)
    elif pilihan == 7:
        os.system("cls")
        print("+----------------------------------------------------+")
        print('''  Terima kasih telah menggunakan program ini 
                tata titi tutu :)''')
        print("+----------------------------------------------------+")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-7.")
