# hasil = divmod(17, 5)

# print(hasil)

# angka = [10, 25, 700, 40, 15]
# hasil = max(angka)

# print(hasil)

# hasil = pow(5, 2)

# print(hasil)

# hasil = pow(3, 2, 2)

# print(hasil)

# angka = 3.14159
# hasil = round(angka, 4)

# print(hasil)

# angka = [10, 20, 30, 40]
# hasil = sum(angka)

# print(hasil)

# angka = [10, 20, 30]
# hasil = sum(angka, 100)

# print(hasil)

# buah = ["Apel", "Jeruk", "Mangga"]
# for index, nama in enumerate(buah):
#     print(f"{index} - {nama}")

# angka = [1, 2, 3, 4]

# hasil = map(lambda x: x * 2, angka)

# print(list(hasil))

# angka = range(1, 1345678)
# print(list(angka)) 

# buah = ["Apel", "Jeruk", "Mangga", "Anggur", "Melon", "bobol", "joko", "kokp"]

# bagian = slice(1, 8, 2)

# print(buah[bagian])

# teks = "   Halo Python   "
# hasil = teks.strip()

# print(hasil)
# # Output: Halo Python

# teks = "***Python***"
# hasil = teks.strip("*")

# print(hasil)
# # Output: Python

# teks = "Saya belajar Java"
# hasil = teks.replace("Java", "Pcvbjky")

# print(hasil)

# teks = "apel apel apel"
# print(teks.replace("apel", "jeruk", 2))

from prettytable import PrettyTable

tabel = PrettyTable()
tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]

tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])
tabel.add_rows([
    ["2609106002", "Hammam Nopal", "Informatika"],
    ["2609106003", "Abimar LLM", "Sistem Informasi"]
])

tabel.align["Nama Mahasiswa"] = "l"
print(tabel)