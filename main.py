saldo = 0

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
        saldo += jumlah
        print(f"Berhasil menambahkan pemasukan sebesar Rp{jumlah:.2f}. Saldo sekarang: Rp{saldo:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
        if jumlah > saldo:
            print("Saldo tidak cukup")
            return
        saldo -= jumlah
        print(f"Berhasil menambahkan pengeluaran sebesar Rp{jumlah:.2f}. Saldo sekarang: Rp{saldo:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def lihat_saldo():
    print("=== Saldo Saat Ini ===")
    print(f"Saldo sekarang: Rp{saldo:,.2f}")

import json
DATA_FILE = "data.json"

def load data():
    global saldo
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            saldo = (data.get("saldo, 0"))
            except (FileNotFoundError, ValueError, json.JSONDecodeError):
                saldo = 0

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump({"saldo": saldo}, f, indent=2)
    except IOError:
        print("Gagal menyimpan data.")       

saldo += jumlah
save_data()
print(f"Berhasil ... Saldo sekarang: Rp{saldo:.2f}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")