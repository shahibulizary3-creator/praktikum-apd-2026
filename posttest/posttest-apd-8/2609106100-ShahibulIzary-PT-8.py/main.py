import os
from data import dataAkun, bersih, username_sudah_ada
from menu_admin import jalankan_menu_admin
from menu_user import jalankan_menu_user

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
            try:
                if registUsername == "" or registPassword == "":
                    raise ValueError("Username dan password tidak boleh kosong.")
                if username_sudah_ada(registUsername):
                    raise ValueError(f"Username '{registUsername}' sudah dipakai. Gunakan username lain.")
            except ValueError as e:
                print(f"\n{e}\n")
            else:
                dataAkun.append({"username": registUsername, "password": registPassword, "role": registRole})
                print(f"\nAkun '{registUsername}' berhasil dibuat. Silakan login.\n")
            finally:
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
        jalankan_menu_admin()
        userLogin = ""
        roleLogin = -1

    else:
        jalankan_menu_user(userLogin)
        userLogin = ""
        roleLogin = -1
