import os

dataAkun = [
{"username": "shahib", "password": "1212", "role": 1},
{"username": "cokib", "password": "123", "role": 0}
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

def hitung_total_stok():
    total = 0                                   
    for nama_alat, info in data_alat.items():
        total += info["stok"]
    return total

def buat_nomor_transaksi():
    nomor_baru = len(data_penjualan) + 1       
    return nomor_baru

def hitung_stok_jenis(nama_jenis):
    total = 0                                   
    for nama_alat, info in data_alat.items(): 
        if info["jenis"] == nama_jenis:
            total += info["stok"]
    return total

def cari_alat_by_jenis(nama_jenis):
    hasil = None
    for nama_alat, info in data_alat.items():
        if info["jenis"] == nama_jenis and hasil is None:
            hasil = nama_alat
    return hasil

def username_sudah_ada(username):
    for akun in dataAkun:
        if akun["username"] == username:
            return True
    return False

def validasi_angka(teks, minimal, maksimal=None):
    try:
        angka = int(teks)
    except ValueError:
        raise ValueError("harus berupa angka bulat.")
    if angka < minimal:
        raise ValueError(f"tidak boleh kurang dari {minimal}.")
    if maksimal is not None and angka > maksimal:
        raise ValueError(f"tidak boleh lebih dari {maksimal}.")
    return angka

def total_rekursif(daftar):
    if len(daftar) == 0:
        return 0
    return daftar[0] + total_rekursif(daftar[1:])