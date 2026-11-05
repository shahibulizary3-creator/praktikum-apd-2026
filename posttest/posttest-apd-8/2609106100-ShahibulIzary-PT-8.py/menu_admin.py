import os
from data import jenisAlat, data_alat, data_penjualan, bersih, hitung_total_stok, cari_alat_by_jenis, validasi_angka
from tampilan import (tampilkan_detail_alat, tampilkan_jenis_alat, tampilkan_pilihan_alat_admin,tampilkan_data_alat_lengkap, tampilkan_data_penjualan) 
def jalankan_menu_admin():
    while True:
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
            tampilkan_jenis_alat()

            pilihJenis = input(f"\nPilih nomor jenis alat (1-{len(jenisAlat)}) : ").strip()
            try:
                pilihJenis = validasi_angka(pilihJenis, 1, len(jenisAlat))
            except ValueError as e:
                print(f"\nNomor jenis tidak valid, {e}\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            jumlahTambah = input("Jumlah alat yang ditambahkan (minimal 1) : ").strip()
            try:
                jumlahTambah = validasi_angka(jumlahTambah, 1)
            except ValueError as e:
                print(f"\nJumlah tidak valid, {e}\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            namaJenis = jenis_keys[pilihJenis - 1]
            modal = jenisAlat[namaJenis]["modal"]
            harga = jenisAlat[namaJenis]["harga"]
            laba = harga - modal

            ketemu_nama = cari_alat_by_jenis(namaJenis)

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
                print("\nAlat baru ditambahkan:")
                tampilkan_detail_alat(namaJenis, data_alat[namaJenis])
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "2":
            os.system(bersih)
            print("DATA ALAT TERDAFTAR")
            if len(data_alat) == 0:
                print("\nBelum ada data alat.\n")
            else:
                print("")
                potensiLaba = tampilkan_data_alat_lengkap()
                print(f"\nTotal jenis alat : {len(data_alat)}")
                print(f"Total stok       : {hitung_total_stok()} unit")
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
            tampilkan_pilihan_alat_admin()

            ubah = input(f"\nPilih nomor alat yang ingin diubah (1-{len(data_alat)}) : ").strip()
            try:
                ubah = validasi_angka(ubah, 1, len(data_alat))
            except ValueError as e:
                print(f"\nNomor tidak valid, {e}\n")
            else:
                nama_lama = alat_keys[ubah - 1]
                info = data_alat[nama_lama]
                print("\nData saat ini:")
                tampilkan_detail_alat(nama_lama, info)

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
                    try:
                        stokBaru = validasi_angka(ubahStok, 0)
                    except ValueError:
                        print("\nStok harus berupa angka bulat (0 atau lebih), stok tidak diubah.")
                    else:
                        data_alat[nama_lama]["stok"] = stokBaru
                        ada_perubahan = True

                if ada_perubahan:
                    print("\nData setelah diubah:")
                    tampilkan_detail_alat(nama_lama, data_alat[nama_lama])
                else:
                    print("\nTidak ada data yang diubah.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "4":
            os.system(bersih)
            print("HAPUS DATA ALAT\n")
            if len(data_alat) == 0:
                print("Belum ada data alat untuk dihapus.\n")
                input("Tekan Enter untuk kembali ke menu...")
                continue

            alat_keys = list(data_alat.keys())
            tampilkan_pilihan_alat_admin()

            hapus = input(f"\nPilih nomor alat yang ingin dihapus (1-{len(data_alat)}) : ").strip()
            try:
                hapus = validasi_angka(hapus, 1, len(data_alat))
            except ValueError as e:
                print(f"\nNomor tidak valid, {e}\n")
            else:
                nama_dihapus = alat_keys[hapus - 1]
                info_dihapus = data_alat.pop(nama_dihapus)
                print(f"\nData '{nama_dihapus}' (jenis {info_dihapus['jenis']}, stok {info_dihapus['stok']} unit) sudah dihapus.\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "5":
            os.system(bersih)
            print("DATA PENJUALAN")
            if len(data_penjualan) == 0:
                print("\nBelum ada transaksi penjualan.\n")
            else:
                print("")
                totalTerjual, totalPendapatan, totalLabaJual = tampilkan_data_penjualan()
                print(f"\nTotal transaksi    : {len(data_penjualan)}")
                print(f"Total alat terjual : {totalTerjual} unit")
                print(f"Total pendapatan   : Rp{totalPendapatan}")
                print(f"Total laba         : Rp{totalLabaJual}\n")
            input("Tekan Enter untuk kembali ke menu...")

        elif pilih == "6":
            print("\nLogout berhasil.\n")
            input("Tekan Enter untuk kembali ke menu utama...")
            return

        else:
            print("\nPilihan tidak valid. Masukkan angka 1-6.\n")
            input("Tekan Enter untuk kembali ke menu...")