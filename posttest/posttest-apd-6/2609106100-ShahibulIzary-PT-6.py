import os

dataAkun = [
{"username": "shahib", "password": "1212", "role": 1},
{"username": "shahib", "password": "123", "role": 0}
]

jenisAlat = {
"Cangkul": {"modal": 30000, "harga": 45000},
"Sekop": {"modal": 25000, "harga": 40000},
"Parang": {"modal": 20000, "harga": 35000},
"Gunting": {"modal": 15000, "harga": 25000}
}

data_alat = {
"Cangkul Baja": {"jenis": "Cangkul", "modal": 30000, "harga": 45000, "laba": 15000, "stok": 20},
"Sekop Besi": {"jenis": "Sekop", "modal": 25000, "harga": 40000, "laba": 15000, "stok": 15},
"Parang Tajam": {"jenis": "Parang", "modal": 20000, "harga": 35000, "laba": 15000, "stok": 10},
"Gunting Dahan": {"jenis": "Gunting", "modal": 15000, "harga": 25000, "laba": 10000, "stok": 12}
}

data_penjualan = {}
bersih = "cls" if os.name == "nt" else "clear"
userLogin = ""
roleLogin = -1

while True:
    os.system(bersih)

    if userLogin == "":
        print("""SISTEM PENJUALAN ALAT KEBUN
1. Register
2. Login
3. Keluar
""")
        inputMenuUtama = input("Pilih menu (1-3) : ").strip()

        if inputMenuUtama == "1":
            os.system(bersih)
            print("DAFTAR AKUN BARU\n")
            registUsername = input("Username baru : ").strip()
            registPassword = input("Password baru : ").strip()
            registRole = 0
            username_terpakai = False
            for akun in dataAkun:
                if akun["username"] == registUsername:
                    username_terpakai = True
            if registUsername == "" or registPassword == "":
                print("\nUsername dan password tidak boleh kosong.\n")
            elif username_terpakai:
                print(f"\nUsername '{registUsername}' sudah dipakai. Gunakan username lain.\n")
            else:
                dataAkun.append({"username": registUsername, "password": registPassword, "role": registRole})
                print(f"\nAkun '{registUsername}' berhasil dibuat. Silakan login.\n")
            input("Tekan Enter untuk kembali ke menu utama...")

        elif inputMenuUtama == "2":
            os.system(bersih)
            print("LOGIN\n")
            inputUsername = input("Username : ").strip()
            inputPassword = input("Password : ").strip()

            login_berhasil = False
            for akun in dataAkun:
                username = akun["username"]
                password = akun["password"]
                role = akun["role"]
                if inputUsername == username and inputPassword == password:
                    login_berhasil = True
                    userLogin = username
                    roleLogin = role

            if not login_berhasil:
                print("\nUsername atau password salah.\n")
                input("Tekan Enter untuk kembali ke menu utama...")
            elif roleLogin == 1:
                print(f"\nLogin sebagai ADMIN. Selamat datang, {userLogin}.\n")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print(f"\nLogin sebagai USER. Selamat datang, {userLogin}.\n")
                input("Tekan Enter untuk melanjutkan...")

        elif inputMenuUtama == "3":
            os.system(bersih)
            print("Program berhenti. Terima kasih.")
            break

        else:
            print("\nPilihan tidak valid. Masukkan angka 1-3.\n")
            input("Tekan Enter untuk kembali ke menu utama...")

    elif roleLogin == 1:
        os.system(bersih)
        print("""MENU ADMIN
1. Tambah alat / tambah stok
2. Tampilkan data alat
3. Ubah data alat
4. Hapus data alat
5. Lihat data penjualan
6. Logout
""")
        pilih = input("Pilih menu (1-6) : ").strip()

        if pilih == "1":
            os.system(bersih)
            print("TAMBAH ALAT / TAMBAH STOK\n")
            print("Jenis alat yang tersedia:")
            jenis_keys = list(jenisAlat.keys())
            for i in range(len(jenis_keys)):
                nama_jenis = jenis_keys[i]
                stokSaatIni = 0
                for nama_alat, a in data_alat.items():
                    if a["jenis"] == nama_jenis:
                        stokSaatIni += a["stok"]
                print(f"{i+1}. {nama_jenis} | Modal: Rp{jenisAlat[nama_jenis]['modal']} | Harga jual: Rp{jenisAlat[nama_jenis]['harga']} | Stok saat ini: {stokSaatIni} unit")

            pilihJenis = input(f"\nPilih nomor jenis alat (1-{len(jenisAlat)}) : ").strip()
            if not (pilihJenis.isdecimal() and 1 <= int(pilihJenis) <= len(jenisAlat)):
                print(f"\nNomor jenis tidak valid. Masukkan angka 1-{len(jenisAlat)}.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahTambah = input("Jumlah alat yang ditambahkan (minimal 1) : ").strip()
            if not (jumlahTambah.isdecimal() and int(jumlahTambah) >= 1):
                print("\nJumlah tidak valid. Masukkan angka bulat minimal 1.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahTambah = int(jumlahTambah)
            namaJenis = jenis_keys[int(pilihJenis) - 1]
            modal = jenisAlat[namaJenis]["modal"]
            harga = jenisAlat[namaJenis]["harga"]
            laba = harga - modal

            ketemu_nama = None
            for nama_alat, a in data_alat.items():
                if a["jenis"] == namaJenis and ketemu_nama is None:
                    ketemu_nama = nama_alat

            if ketemu_nama is not None:
                data_alat[ketemu_nama]["stok"] += jumlahTambah
                print(f"""
Alat '{ketemu_nama}' ({namaJenis}) sudah ada, stok ditambah {jumlahTambah} unit.
Stok sekarang : {data_alat[ketemu_nama]['stok']} unit
""")
            else:
                data_alat[namaJenis] = {
                    "jenis": namaJenis,
                    "modal": modal,
                    "harga": harga,
                    "laba": laba,
                    "stok": jumlahTambah
                }
                print(f"""
Alat baru ditambahkan:
Nama           : {namaJenis}
Jenis          : {namaJenis}
Modal per unit : Rp{modal}
Harga per unit : Rp{harga}
Laba per unit  : Rp{laba}
Stok           : {jumlahTambah} unit
""")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "2":
            os.system(bersih)
            print("DATA ALAT TERDAFTAR")
            if len(data_alat) == 0:
                print("\nBelum ada data alat.\n")
            else:
                totalStok = 0
                potensiLaba = 0
                i = 0
                for nama, info in data_alat.items():
                    print(f"""
Alat ke-{i+1}
Nama           : {nama}
Jenis          : {info['jenis']}
Modal per unit : Rp{info['modal']}
Harga per unit : Rp{info['harga']}
Laba per unit  : Rp{info['laba']}
Stok           : {info['stok']} unit""")
                    totalStok += info["stok"]
                    potensiLaba += info["laba"] * info["stok"]
                    i += 1
                print(f"\nTotal jenis alat : {len(data_alat)}")
                print(f"Total stok       : {totalStok} unit")
                print(f"Potensi laba     : Rp{potensiLaba} (jika semua stok terjual)\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "3":
            os.system(bersih)
            print("UBAH DATA ALAT\n")
            if len(data_alat) == 0:
                print("Belum ada data alat untuk diubah.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            alat_keys = list(data_alat.keys())
            for i in range(len(alat_keys)):
                nama = alat_keys[i]
                info = data_alat[nama]
                print(f"{i+1}. Nama: {nama} | Jenis: {info['jenis']} | Stok: {info['stok']} unit")

            ubah = input(f"\nPilih nomor alat yang ingin diubah (1-{len(data_alat)}) : ").strip()
            if ubah.isdecimal() and 1 <= int(ubah) <= len(data_alat):
                nama_lama = alat_keys[int(ubah) - 1]
                info = data_alat[nama_lama]
                print(f"""
Data saat ini:
Nama           : {nama_lama}
Jenis          : {info['jenis']}
Modal per unit : Rp{info['modal']}
Harga per unit : Rp{info['harga']}
Laba per unit  : Rp{info['laba']}
Stok           : {info['stok']} unit
""")
                ubahNama = input("Nama baru (kosongkan jika tidak diubah) : ").strip()
                ubahJenis = input("Jenis baru - Cangkul/Sekop/Parang/Gunting (kosongkan jika tidak diubah) : ").strip().capitalize()
                ubahStok = input("Stok baru dalam unit (kosongkan jika tidak diubah) : ").strip()

                ada_perubahan = False

                if ubahNama:
                    if ubahNama != nama_lama:
                        data_alat[ubahNama] = data_alat.pop(nama_lama)
                        nama_lama = ubahNama
                    ada_perubahan = True

                if ubahJenis:
                    found = False
                    for j_name, j_val in jenisAlat.items():
                        if j_name == ubahJenis:
                            data_alat[nama_lama]["jenis"] = ubahJenis
                            data_alat[nama_lama]["modal"] = j_val["modal"]
                            data_alat[nama_lama]["harga"] = j_val["harga"]
                            data_alat[nama_lama]["laba"] = j_val["harga"] - j_val["modal"]
                            found = True
                            ada_perubahan = True
                            break
                    if not found:
                        print(f"\nJenis '{ubahJenis}' tidak dikenali, jenis tidak diubah.")

                if ubahStok != "":
                    if ubahStok.isdecimal():
                        data_alat[nama_lama]["stok"] = int(ubahStok)
                        ada_perubahan = True
                    else:
                        print("\nStok harus berupa angka bulat (0 atau lebih), stok tidak diubah.")

                if ada_perubahan:
                    info_terkini = data_alat[nama_lama]
                    print(f"""
Data setelah diubah:
Nama           : {nama_lama}
Jenis          : {info_terkini['jenis']}
Modal per unit : Rp{info_terkini['modal']}
Harga per unit : Rp{info_terkini['harga']}
Laba per unit  : Rp{info_terkini['laba']}
Stok           : {info_terkini['stok']} unit
""")
                else:
                    print("\nTidak ada data yang diubah.\n")
            else:
                print(f"\nNomor tidak valid. Masukkan angka 1-{len(data_alat)}.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "4":
            os.system(bersih)
            print("HAPUS DATA ALAT\n")
            if len(data_alat) == 0:
                print("Belum ada data alat untuk dihapus.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            alat_keys = list(data_alat.keys())
            for i in range(len(alat_keys)):
                nama = alat_keys[i]
                info = data_alat[nama]
                print(f"{i+1}. Nama: {nama} | Jenis: {info['jenis']} | Stok: {info['stok']} unit")

            hapus = input(f"\nPilih nomor alat yang ingin dihapus (1-{len(data_alat)}) : ").strip()
            if hapus.isdecimal() and 1 <= int(hapus) <= len(data_alat):
                nama_dihapus = alat_keys[int(hapus) - 1]
                info_dihapus = data_alat.pop(nama_dihapus)
                print(f"\nData '{nama_dihapus}' (jenis {info_dihapus['jenis']}, stok {info_dihapus['stok']} unit) sudah dihapus.\n")
            else:
                print(f"\nNomor tidak valid. Masukkan angka 1-{len(data_alat)}.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "5":
            os.system(bersih)
            print("DATA PENJUALAN")
            if len(data_penjualan) == 0:
                print("\nBelum ada transaksi penjualan.\n")
            else:
                totalTerjual = 0
                totalPendapatan = 0
                totalLabaJual = 0
                for t_id, t in data_penjualan.items():
                    print(f"""
Transaksi ke-{t_id}
Pembeli      : {t['pembeli']}
Alat         : {t['nama_alat']} ({t['jenis']})
Jumlah       : {t['jumlah']} unit
Harga/unit   : Rp{t['harga_unit']}
Total bayar  : Rp{t['total_bayar']}
Laba         : Rp{t['laba']}""")
                    totalTerjual += t['jumlah']
                    totalPendapatan += t['total_bayar']
                    totalLabaJual += t['laba']
                print(f"\nTotal transaksi    : {len(data_penjualan)}")
                print(f"Total alat terjual : {totalTerjual} unit")
                print(f"Total pendapatan   : Rp{totalPendapatan}")
                print(f"Total laba         : Rp{totalLabaJual}\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "6":
            print("\nLogout berhasil.\n")
            input("Tekan Enter untuk kembali ke menu utama...")
            userLogin = ""
            roleLogin = -1

        else:
            print("\nPilihan tidak valid. Masukkan angka 1-6.\n")
            input("Tekan Enter untuk kembali ke menu...")

    else:
        os.system(bersih)
        print("""MENU PENGGUNA
1. Lihat daftar alat dijual
2. Beli alat
3. Riwayat pembelian saya
4. Logout
""")
        pilih = input("Pilih menu (1-4) : ").strip()

        if pilih == "1":
            os.system(bersih)
            print("DAFTAR ALAT DIJUAL\n")
            if len(data_alat) == 0:
                print("Belum ada alat yang dijual.\n")
            else:
                alat_keys = list(data_alat.keys())
                for i in range(len(alat_keys)):
                    nama = alat_keys[i]
                    info = data_alat[nama]
                    if info["stok"] == 0:
                        teksStok = "HABIS"
                    else:
                        teksStok = f"{info['stok']} unit"
                    print(f"{i+1}. Nama: {nama} | Harga: Rp{info['harga']} | Stok: {teksStok}")
                print("")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "2":
            os.system(bersih)
            print("BELI ALAT\n")
            if len(data_alat) == 0:
                print("Belum ada alat yang dijual.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            alat_keys = list(data_alat.keys())
            for i in range(len(alat_keys)):
                nama = alat_keys[i]
                info = data_alat[nama]
                if info["stok"] == 0:
                    teksStok = "HABIS"
                else:
                    teksStok = f"{info['stok']} unit"
                print(f"{i+1}. Nama: {nama} | Harga: Rp{info['harga']} | Stok: {teksStok}")

            beli = input(f"\nPilih nomor alat yang ingin dibeli (1-{len(data_alat)}) : ").strip()
            if not (beli.isdecimal() and 1 <= int(beli) <= len(data_alat)):
                print(f"\nNomor tidak valid. Masukkan angka 1-{len(data_alat)}.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            namaAlatDibeli = alat_keys[int(beli) - 1]
            alatDibeli = data_alat[namaAlatDibeli]

            if alatDibeli["stok"] == 0:
                print(f"\nStok '{namaAlatDibeli}' sedang habis.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahBeli = input(f"Jumlah yang ingin dibeli (1-{alatDibeli['stok']}) : ").strip()
            if not (jumlahBeli.isdecimal() and 1 <= int(jumlahBeli) <= alatDibeli["stok"]):
                print(f"\nJumlah tidak valid. Masukkan angka 1-{alatDibeli['stok']}.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahBeli = int(jumlahBeli)
            totalBayar = alatDibeli["harga"] * jumlahBeli
            print(f"""
Rincian pembelian:
Alat         : {namaAlatDibeli} ({alatDibeli['jenis']})
Jumlah       : {jumlahBeli} unit
Harga/unit   : Rp{alatDibeli['harga']}
Total bayar  : Rp{totalBayar}
""")
            konfirmasi = input("Lanjutkan pembelian? (y = ya, n = batal) : ").strip().lower()

            if konfirmasi == "y":
                alatDibeli["stok"] -= jumlahBeli
                nomorTransaksi = len(data_penjualan) + 1
                data_penjualan[nomorTransaksi] = {
                    "pembeli": userLogin,
                    "nama_alat": namaAlatDibeli,
                    "jenis": alatDibeli["jenis"],
                    "jumlah": jumlahBeli,
                    "harga_unit": alatDibeli["harga"],
                    "total_bayar": totalBayar,
                    "laba": alatDibeli["laba"] * jumlahBeli
                }
                print(f"""
Pembelian berhasil:
No. transaksi : {nomorTransaksi}
Alat          : {namaAlatDibeli} ({alatDibeli['jenis']})
Jumlah        : {jumlahBeli} unit
Total bayar   : Rp{totalBayar}
Sisa stok     : {alatDibeli['stok']} unit
""")
            elif konfirmasi == "n":
                print("\nPembelian dibatalkan.\n")
            else:
                print("\nJawaban harus 'y' atau 'n'. Pembelian dibatalkan.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "3":
            os.system(bersih)
            print("RIWAYAT PEMBELIAN SAYA")
            ada_riwayat = False
            totalBelanja = 0
            for t_id, t in data_penjualan.items():
                if t["pembeli"] == userLogin:
                    ada_riwayat = True
                    print(f"""
Transaksi ke-{t_id}
Alat         : {t['nama_alat']} ({t['jenis']})
Jumlah       : {t['jumlah']} unit
Harga/unit   : Rp{t['harga_unit']}
Total bayar  : Rp{t['total_bayar']}""")
                    totalBelanja += t['total_bayar']
            if ada_riwayat:
                print(f"\nTotal belanja saya : Rp{totalBelanja}\n")
            else:
                print("\nAnda belum pernah membeli alat.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "4":
            print("\nLogout berhasil.\n")
            input("Tekan Enter untuk kembali ke menu utama...")
            userLogin = ""
            roleLogin = -1

        else:
            print("\nPilihan tidak valid. Masukkan angka 1-4.\n")
            input("Tekan Enter untuk kembali ke menu...")