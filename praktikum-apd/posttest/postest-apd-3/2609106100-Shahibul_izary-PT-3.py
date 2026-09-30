print ("Selamat datang di penyewaan PlayStation")
print ("Silahkan login terlebih dahulu")

nama_benar = "sohib"
nim_benar = 100

username = str (input("username : "))
password = int (input("nim anda : "))

if username == nama_benar and nim_benar :
    print ("login berhasil, selamat datang", nama_benar)

    print ("silahkan pilih menu konsol")
    print ("MENU KONSOL")
    print ("1. PS4 : Rp 10.000/jam")
    print ("2. PS4 Pro : Rp 15.000/jam")
    print ("3. PS5 : Rp 10.000/jam")

    pilihan_konsol = int (input ("jenis konsol yang kamu mau : "))
    if pilihan_konsol == 1 or pilihan_konsol == 2 or pilihan_konsol == 3 :
        if pilihan_konsol == 1 :
            jenis_konsol = "PS4"
            harga_per_jam = 10000
        elif pilihan_konsol == 2 :
            jenis_konsol = "PS4 Pro"
            harga_per_jam = 15000
        else :
            jenis_konsol = "PS5"
            harga_per_jam = 20000

        durasi_sewa = int (input("mau sewa berapa jam : "))

        if durasi_sewa >= 5 :
            persen_diskon = 0.08
        elif durasi_sewa >= 3 :
            persen_diskon = 0.05
        else :
            persen_diskon = 0.00

        total_harga = harga_per_jam * durasi_sewa
        diskon_durasi = total_harga * persen_diskon

        hari_sewa = str (input("apakah sewa saat hari weeekend? (iya/tidak):"))
        if hari_sewa == "iya" : 
            tambahan_weekend = total_harga * 0.10
        else :
            tambahan_weekend = total_harga * 0

        total_bayar = total_harga - diskon_durasi + tambahan_weekend

        print ("-------- STRUK ANDA --------")
        print ("nama penyewa : ", nama_benar)
        print ("nim penyewa : ",nim_benar)
        print ("jesis konsol yang dipilih : ",jenis_konsol)
        print ("menyewa selama : ", durasi_sewa, "jam")
        print ("total harga :", total_harga)
        print ("diskon durasi : ", diskon_durasi)
        print ("tambahan harga weekend : ", tambahan_weekend)
        print ("total harga yang harus anda bayar : ", total_bayar)
        print (" ---- TERIMAKASIH SELAMAT SELAMAT BERMAIN ---- ")

    else :
        print ("pilihan konsol tidak valid!!! program dihentikan")

else :
    print ("login gagal, nama/nim anda salah!!! program di hentikan")