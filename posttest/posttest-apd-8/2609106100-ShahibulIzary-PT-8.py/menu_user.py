import os
from data import data_alat, data_penjualan, bersih, buat_nomor_transaksi, validasi_angka, total_rekursif
from tampilan import tampilkan_daftar_pembeli, tampilkan_rincian, tampilkan_riwayat_pembelian

def jalankan_menu_user(userLogin):
    while True:
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
                tampilkan_daftar_pembeli()
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
            tampilkan_daftar_pembeli()

            beli = input(f"\nPilih nomor alat yang ingin dibeli (1-{len(data_alat)}) : ").strip()
            try:
                beli = validasi_angka(beli, 1, len(data_alat))
            except ValueError as e:
                print(f"\nNomor tidak valid, {e}\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            namaAlatDibeli = alat_keys[beli - 1]
            alatDibeli = data_alat[namaAlatDibeli]

            if alatDibeli["stok"] == 0:
                print(f"\nStok '{namaAlatDibeli}' sedang habis.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahBeli = input(f"Jumlah yang ingin dibeli (1-{alatDibeli['stok']}) : ").strip()
            try:
                jumlahBeli = validasi_angka(jumlahBeli, 1, alatDibeli["stok"])
            except ValueError as e:
                print(f"\nJumlah tidak valid, {e}\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            totalBayar = alatDibeli["harga"] * jumlahBeli
            print("\nRincian pembelian:")
            tampilkan_rincian([
                ("Alat", f"{namaAlatDibeli} ({alatDibeli['jenis']})"),
                ("Jumlah", f"{jumlahBeli} unit"),
                ("Harga/unit", f"Rp{alatDibeli['harga']}"),
                ("Total bayar", f"Rp{totalBayar}")
            ])
            konfirmasi = input("Lanjutkan pembelian? (y = ya, n = batal) : ").strip().lower()

            if konfirmasi == "y":
                alatDibeli["stok"] -= jumlahBeli
                nomorTransaksi = buat_nomor_transaksi()
                data_penjualan[nomorTransaksi] = {
                    "pembeli": userLogin,
                    "nama_alat": namaAlatDibeli,
                    "jenis": alatDibeli["jenis"],
                    "jumlah": jumlahBeli,
                    "harga_unit": alatDibeli["harga"],
                    "total_bayar": totalBayar,
                    "laba": alatDibeli["laba"] * jumlahBeli
                }
                print("\nPembelian berhasil:")
                tampilkan_rincian([
                    ("No. transaksi", nomorTransaksi),
                    ("Alat", f"{namaAlatDibeli} ({alatDibeli['jenis']})"),
                    ("Jumlah", f"{jumlahBeli} unit"),
                    ("Total bayar", f"Rp{totalBayar}"),
                    ("Sisa stok", f"{alatDibeli['stok']} unit")
                ])
            elif konfirmasi == "n":
                print("\nPembelian dibatalkan.\n")
            else:
                print("\nJawaban harus 'y' atau 'n'. Pembelian dibatalkan.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "3":
            os.system(bersih)
            print("RIWAYAT PEMBELIAN SAYA\n")
            daftarTotalBayar = tampilkan_riwayat_pembelian(userLogin)
            if len(daftarTotalBayar) > 0:
                totalBelanja = total_rekursif(daftarTotalBayar)
                print(f"\nTotal belanja saya : Rp{totalBelanja}\n")
            else:
                print("Anda belum pernah membeli alat.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "4":
            print("\nLogout berhasil.\n")
            input("Tekan Enter untuk kembali ke menu utama...")
            return

        else:
            print("\nPilihan tidak valid. Masukkan angka 1-4.\n")
            input("Tekan Enter untuk kembali ke menu...")