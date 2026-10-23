# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# print(f"Luas persegi panjang:", {luas_persegi_panjang()})

# def luas_persegi_panjang(sisi, lebar):
#     luas = sisi * lebar
#     return luas
# print("Luas persegi panjang :", luas_persegi_panjang(7,8,))

# def pengumuman(matkul):
#     print(f"Hari ini proyek akhir {matkul}")

# pengumuman("apd")
# pengumuman("kukang")
# pengumuman("kalkulus")
# pengumuman("hddnkxihugdchsjuhxgvhcd nskjixhcgvbnsxjdbuuvdgskjchucudbcjdugugfefewhnjchchdhdjcnjc")

# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")
# sapa_pengguna("Citra")

# nama = "Larry"
# prodi = "Informatika"

# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)
# data()
# print("Nama:", nama)
# print("Prodi:", prodi)

# def hitung_mundur (n) :
#     if n == 0:
#         print("MATI")
#     else:
#         print(n)
#         hitung_mundur(n-500)

# hitung_mundur(5000)

# buku = []

# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#         for indeks in range(len(buku)):
#             print(indeks, "|", buku[indeks])

# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")

# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")

#     menu = input("PILIH MENU> ")
#     print("\n")

#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")

# while (True):
#     tampilkan_menu()

try:
    umur = int(input('Masukkan Angka : '))
except ValueError:
    print("umur yang dimasukkan tidak seusai tipe data : ")
else:
    print(f"umur kamu adalah : ", umur)

