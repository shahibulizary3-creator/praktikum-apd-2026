import os

dataAkun = [["shahib", "1212", 1], ["shahib", "123", 0]]
jenisAlat = [
    ["Cangkul", 30000, 45000],
    ["Sekop", 25000, 40000],
    ["Parang", 20000, 35000],
    ["Gunting", 15000, 25000],
]
data_alat = [
    ["Cangkul Baja", "Cangkul", 30000, 45000, 15000, 20],
    ["Sekop Besi", "Sekop", 25000, 40000, 15000, 15],
    ["Parang Tajam", "Parang", 20000, 35000, 15000, 10],
    ["Gunting Dahan", "Gunting", 15000, 25000, 10000, 12],
]
data_penjualan = []
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
        if akun[0] == registUsername:
          username_terpakai = True
      if registUsername == "" or registPassword == "":
        print("\nUsername dan password tidak boleh kosong.\n")
      elif username_terpakai:
        print(
            f"\nUsername '{registUsername}' sudah dipakai. Gunakan username"
            " lain.\n"
        )
      else:
        dataAkun.append([registUsername, registPassword, registRole])
        print(f"\nAkun '{registUsername}' berhasil dibuat. Silakan login.\n")
      input("Tekan Enter untuk kembali ke menu utama...")

    elif inputMenuUtama == "2":
      os.system(bersih)
      print("LOGIN\n")
      inputUsername = input("Username : ").strip()
      inputPassword = input("Password : ").strip()

      login_berhasil = False
      for akun in dataAkun:
        username, password, role = akun
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
      for i in range(len(jenisAlat)):
        stokSaatIni = 0
        for a in data_alat:
          if a[1] == jenisAlat[i][0]:
            stokSaatIni += a[5]
        print(
            f"{i+1}. {jenisAlat[i][0]} | Modal: Rp{jenisAlat[i][1]} | Harga jual:"
            f" Rp{jenisAlat[i][2]} | Stok saat ini: {stokSaatIni} unit"
        )

      pilihJenis = input(
          f"\nPilih nomor jenis alat (1-{len(jenisAlat)}) : "
      ).strip()
      if not (pilihJenis.isdecimal() and 1 <= int(pilihJenis) <= len(jenisAlat)):
        print(f"\nNomor jenis tidak valid. Masukkan angka 1-{len(jenisAlat)}.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      jumlahTambah = input(
          "Jumlah alat yang ditambahkan (minimal 1) : "
      ).strip()
      if not (jumlahTambah.isdecimal() and int(jumlahTambah) >= 1):
        print("\nJumlah tidak valid. Masukkan angka bulat minimal 1.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      jumlahTambah = int(jumlahTambah)
      namaJenis, modal, harga = jenisAlat[int(pilihJenis) - 1]
      laba = harga - modal

      ketemu = -1
      for i in range(len(data_alat)):
        if data_alat[i][1] == namaJenis and ketemu == -1:
          ketemu = i

      if ketemu >= 0:
        data_alat[ketemu][5] += jumlahTambah
        print(f"""
Alat '{data_alat[ketemu][0]}' ({namaJenis}) sudah ada, stok ditambah {jumlahTambah} unit.
Stok sekarang : {data_alat[ketemu][5]} unit
""")
      else:
        data_alat.append(
            [namaJenis, namaJenis, modal, harga, laba, jumlahTambah]
        )
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
        for i in range(len(data_alat)):
          nama, jenis, modal, harga, laba, stok = data_alat[i]
          print(f"""
Alat ke-{i+1}
  Nama           : {nama}
  Jenis          : {jenis}
  Modal per unit : Rp{modal}
  Harga per unit : Rp{harga}
  Laba per unit  : Rp{laba}
  Stok           : {stok} unit""")
          totalStok += stok
          potensiLaba += laba * stok
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

      for i in range(len(data_alat)):
        print(
            f"{i+1}. Nama: {data_alat[i][0]} | Jenis: {data_alat[i][1]} | Stok:"
            f" {data_alat[i][5]} unit"
        )

      ubah = input(
          f"\nPilih nomor alat yang ingin diubah (1-{len(data_alat)}) : "
      ).strip()
      if ubah.isdecimal() and 1 <= int(ubah) <= len(data_alat):
        ngubah = int(ubah) - 1
        nama, jenis, modal, harga, laba, stok = data_alat[ngubah]
        print(f"""
Data saat ini:
  Nama           : {nama}
  Jenis          : {jenis}
  Modal per unit : Rp{modal}
  Harga per unit : Rp{harga}
  Laba per unit  : Rp{laba}
  Stok           : {stok} unit
""")
        ubahNama = input("Nama baru (kosongkan jika tidak diubah) : ").strip()
        ubahJenis = input(
            "Jenis baru - Cangkul/Sekop/Parang/Gunting (kosongkan jika tidak"
            " diubah) : "
        ).strip().capitalize()
        ubahStok = input(
            "Stok baru dalam unit (kosongkan jika tidak diubah) : "
        ).strip()

        ada_perubahan = False

        if ubahNama:
          data_alat[ngubah][0] = ubahNama
          ada_perubahan = True

        if ubahJenis:
          found = False
          for alat in jenisAlat:
            if alat[0] == ubahJenis:
              data_alat[ngubah][1] = ubahJenis
              data_alat[ngubah][2] = alat[1]
              data_alat[ngubah][3] = alat[2]
              data_alat[ngubah][4] = alat[2] - alat[1]
              found = True
              ada_perubahan = True
              break
          if not found:
            print(f"\nJenis '{ubahJenis}' tidak dikenali, jenis tidak diubah.")

        if ubahStok != "":
          if ubahStok.isdecimal():
            data_alat[ngubah][5] = int(ubahStok)
            ada_perubahan = True
          else:
            print(
                "\nStok harus berupa angka bulat (0 atau lebih), stok tidak"
                " diubah."
            )

        if ada_perubahan:
          nama, jenis, modal, harga, laba, stok = data_alat[ngubah]
          print(f"""
Data setelah diubah:
  Nama           : {nama}
  Jenis          : {jenis}
  Modal per unit : Rp{modal}
  Harga per unit : Rp{harga}
  Laba per unit  : Rp{laba}
  Stok           : {stok} unit
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

      for i in range(len(data_alat)):
        print(
            f"{i+1}. Nama: {data_alat[i][0]} | Jenis: {data_alat[i][1]} | Stok:"
            f" {data_alat[i][5]} unit"
        )

      hapus = input(
          f"\nPilih nomor alat yang ingin dihapus (1-{len(data_alat)}) : "
      ).strip()
      if hapus.isdecimal() and 1 <= int(hapus) <= len(data_alat):
        dihapus = data_alat[int(hapus) - 1]
        del data_alat[int(hapus) - 1]
        print(
            f"\nData '{dihapus[0]}' (jenis {dihapus[1]}, stok {dihapus[5]} unit)"
            " sudah dihapus.\n"
        )
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
        for t in data_penjualan:
          print(f"""
Transaksi ke-{t[0]}
  Pembeli      : {t[1]}
  Alat         : {t[2]} ({t[3]})
  Jumlah       : {t[4]} unit
  Harga/unit   : Rp{t[5]}
  Total bayar  : Rp{t[6]}
  Laba         : Rp{t[7]}""")
          totalTerjual += t[4]
          totalPendapatan += t[6]
          totalLabaJual += t[7]
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
        for i in range(len(data_alat)):
          if data_alat[i][5] == 0:
            teksStok = "HABIS"
          else:
            teksStok = f"{data_alat[i][5]} unit"
          print(
              f"{i+1}. Nama: {data_alat[i][0]} | Harga: Rp{data_alat[i][3]} |"
              f" Stok: {teksStok}"
          )
        print("")
      input("Tekan Enter untuk kembali ke menu...")

    elif pilih == "2":
      os.system(bersih)
      print("BELI ALAT\n")
      if len(data_alat) == 0:
        print("Belum ada alat yang dijual.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      for i in range(len(data_alat)):
        if data_alat[i][5] == 0:
          teksStok = "HABIS"
        else:
          teksStok = f"{data_alat[i][5]} unit"
        print(
            f"{i+1}. Nama: {data_alat[i][0]} | Harga: Rp{data_alat[i][3]} | Stok:"
            f" {teksStok}"
        )

      beli = input(
          f"\nPilih nomor alat yang ingin dibeli (1-{len(data_alat)}) : "
      ).strip()
      if not (beli.isdecimal() and 1 <= int(beli) <= len(data_alat)):
        print(f"\nNomor tidak valid. Masukkan angka 1-{len(data_alat)}.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      alatDibeli = data_alat[int(beli) - 1]
      if alatDibeli[5] == 0:
        print(f"\nStok '{alatDibeli[0]}' sedang habis.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      jumlahBeli = input(
          f"Jumlah yang ingin dibeli (1-{alatDibeli[5]}) : "
      ).strip()
      if not (jumlahBeli.isdecimal() and 1 <= int(jumlahBeli) <= alatDibeli[5]):
        print(f"\nJumlah tidak valid. Masukkan angka 1-{alatDibeli[5]}.\n")
        input("Tekan Enter untuk kembali ke menu...")
        continue

      jumlahBeli = int(jumlahBeli)
      totalBayar = alatDibeli[3] * jumlahBeli
      print(f"""
Rincian pembelian:
  Alat         : {alatDibeli[0]} ({alatDibeli[1]})
  Jumlah       : {jumlahBeli} unit
  Harga/unit   : Rp{alatDibeli[3]}
  Total bayar  : Rp{totalBayar}
""")
      konfirmasi = input(
          "Lanjutkan pembelian? (y = ya, n = batal) : "
      ).strip().lower()

      if konfirmasi == "y":
        alatDibeli[5] -= jumlahBeli
        nomorTransaksi = len(data_penjualan) + 1
        data_penjualan.append([
            nomorTransaksi,
            userLogin,
            alatDibeli[0],
            alatDibeli[1],
            jumlahBeli,
            alatDibeli[3],
            totalBayar,
            alatDibeli[4] * jumlahBeli,
        ])
        print(f"""
Pembelian berhasil:
  No. transaksi : {nomorTransaksi}
  Alat          : {alatDibeli[0]} ({alatDibeli[1]})
  Jumlah        : {jumlahBeli} unit
  Total bayar   : Rp{totalBayar}
  Sisa stok     : {alatDibeli[5]} unit
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
      for t in data_penjualan:
        if t[1] == userLogin:
          ada_riwayat = True
          print(f"""
Transaksi ke-{t[0]}
  Alat         : {t[2]} ({t[3]})
  Jumlah       : {t[4]} unit
  Harga/unit   : Rp{t[5]}
  Total bayar  : Rp{t[6]}""")
          totalBelanja += t[6]
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