from prettytable import PrettyTable
from data import data_alat, data_penjualan, jenisAlat, hitung_stok_jenis

def tampilkan_daftar_pembeli():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Harga", "Stok"]
    alat_keys = list(data_alat.keys())
    for i in range(len(alat_keys)):
        nama = alat_keys[i]
        info = data_alat[nama]
        if info["stok"] == 0:
            teksStok = "HABIS"
        else:
            teksStok = f"{info['stok']} unit"
        tabel.add_row([i+1, nama, f"Rp{info['harga']}", teksStok])
    print(tabel)

def tampilkan_detail_alat(nama, info):
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Nilai"]
    tabel.add_row(["Nama", nama])
    tabel.add_row(["Jenis", info['jenis']])
    tabel.add_row(["Modal per unit", f"Rp{info['modal']}"])
    tabel.add_row(["Harga per unit", f"Rp{info['harga']}"])
    tabel.add_row(["Laba per unit", f"Rp{info['laba']}"])
    tabel.add_row(["Stok", f"{info['stok']} unit"])
    print(tabel)
    print("")

def tampilkan_jenis_alat():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Jenis", "Modal", "Harga jual", "Stok saat ini"]
    jenis_keys = list(jenisAlat.keys())
    for i in range(len(jenis_keys)):
        nama_jenis = jenis_keys[i]
        stokSaatIni = hitung_stok_jenis(nama_jenis)
        tabel.add_row([i+1, nama_jenis, f"Rp{jenisAlat[nama_jenis]['modal']}", f"Rp{jenisAlat[nama_jenis]['harga']}", f"{stokSaatIni} unit"])
    print(tabel)

def tampilkan_pilihan_alat_admin():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Jenis", "Stok"]
    alat_keys = list(data_alat.keys())
    for i in range(len(alat_keys)):
        nama = alat_keys[i]
        info = data_alat[nama]
        tabel.add_row([i+1, nama, info['jenis'], f"{info['stok']} unit"])
    print(tabel)

def tampilkan_data_alat_lengkap():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Jenis", "Modal per unit", "Harga per unit", "Laba per unit", "Stok"]
    potensiLaba = 0
    i = 0
    for nama, info in data_alat.items():
        tabel.add_row([i+1, nama, info['jenis'], f"Rp{info['modal']}", f"Rp{info['harga']}", f"Rp{info['laba']}", f"{info['stok']} unit"])
        potensiLaba += info["laba"] * info["stok"]
        i += 1
    print(tabel)
    return potensiLaba

def tampilkan_data_penjualan():
    tabel = PrettyTable()
    tabel.field_names = ["Transaksi", "Pembeli", "Alat", "Jumlah", "Harga/unit", "Total bayar", "Laba"]
    totalTerjual = 0
    totalPendapatan = 0
    totalLabaJual = 0
    for t_id, t in data_penjualan.items():
        tabel.add_row([t_id, t['pembeli'], f"{t['nama_alat']} ({t['jenis']})", f"{t['jumlah']} unit", f"Rp{t['harga_unit']}", f"Rp{t['total_bayar']}", f"Rp{t['laba']}"])
        totalTerjual += t['jumlah']
        totalPendapatan += t['total_bayar']
        totalLabaJual += t['laba']
    print(tabel)
    return totalTerjual, totalPendapatan, totalLabaJual

def tampilkan_riwayat_pembelian(userLogin):
    tabel = PrettyTable()
    tabel.field_names = ["Transaksi", "Alat", "Jumlah", "Harga/unit", "Total bayar"]
    daftarTotalBayar = []
    for t_id, t in data_penjualan.items():
        if t["pembeli"] == userLogin:
            tabel.add_row([t_id, f"{t['nama_alat']} ({t['jenis']})", f"{t['jumlah']} unit", f"Rp{t['harga_unit']}", f"Rp{t['total_bayar']}"])
            daftarTotalBayar.append(t['total_bayar'])
    if len(daftarTotalBayar) > 0:
        print(tabel)
    return daftarTotalBayar

def tampilkan_rincian(daftar_baris):
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Nilai"]
    for baris in daftar_baris:
        tabel.add_row([baris[0], baris[1]])
    print(tabel)
    print("")