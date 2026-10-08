# lemari = ["baju", "celana", 69, 7.2, True]
# print ("sebelum di append")
# print (lemari)
# lemari.append("KTP")
# print("sesudah di append")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True]
# print ("sebelum di extend")
# print (lemari)
# lemari.extend(["KTP", "sepatu", "dompet"])
# print("sesudah di extend")
# print(lemari)


# lemari = ["baju", "celana", 69, 7.2, True]
# print ("sebelum di insert")
# print (lemari)
# lemari.insert(1, "KTP")
# print("sesudah di insert")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]

# for item in lemari :
#     print (item)

# for index, item in enumerate(lemari):
#     print(f"index ke-"())

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]

# print("sebelum diuabh")
# print(lemari)
# lemari[4] = "celana panjang"

# print("sesudah diuabh")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]
# print(lemari)
# # lemari.remove("baju")
# print(lemari)
# sisa = lemari.pop(2)
# print(sisa)

# angka1 = [1,3,5]
# angka2 = [2,4,6]
# gabungan = angka1 + angka2
# print (gabungan)

# ulang = angka1*3
# print (ulang)

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]
# angka1 = [ [1,2], [3,4], ]
# print (angka1[0][1])


# tuple
# angka = (1, 2, 3, "halo", True) 
# ubah = list(angka)
# ubah.append("hai")

# angka = tuple(ubah)
# print (angka)

lemari = ("baju", "celana", "sepatu")
(atasan, *bawahan) = lemari

print(bawahan)