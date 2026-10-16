# kartu = {"merah", "merah", "biru", "hijau"}

# print(kartu)

# matkul = ["apd", "orsikom", "apd", "kalkulus", "logmat"]
# sks = set(matkul)
# print(sks)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# buah = {"apel", "mangga", "jeruk"}
# buah.discard("mangga")
# print(buah) 

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal", "fina"}
# gabung = aslab1.intersection(aslab2)
# print(gabung)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }
# # print(f"Nama saya adalah {Biodata['Nama']}")
# # print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)

# for i in game.values():
#     print(i)

# for key, value in game.items():
#     print(f"{key} adalah jenis game {value}")

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# # game["resident evil"] = "horror"
# # print(game)

# # game.update({"resident evil" : "horror"})
# # print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# aset = {
#     "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# print(aset)
# buang = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(buang)

# print(aset)
# aset.clear()
# print(aset)

# print("Panjang dictionary :", len(aset))
# print(len(aset))

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print("Panjang dictionary :", len(aset))
# print(len(aset))

poli_umum = {"Andi", "Budi", "Citra", "Doni"}
poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
gabung = poli_umum.union(poli_gigi)
print (gabung)