import json
from datetime import datetime

DATA_FILE = "data.json"

saldo = 0.0
transactions = []


def load_data():
    global saldo, transactions
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            saldo = float(data.get("saldo", 0))
            transactions = data.get("transactions", [])
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        saldo = 0.0
        transactions = []


def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump({"saldo": saldo, "transactions": transactions}, f, indent=2)
    except IOError:
        print("Gagal menyimpan data.")


def tambah_pemasukan():
    global saldo, transactions
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
        saldo += jumlah
        transaksi = {
            "type": "pemasukan",
            "amount": jumlah,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        transactions.append(transaksi)
        save_data()
        print(f"Berhasil menambahkan pemasukan sebesar Rp{jumlah:,.2f}. Saldo sekarang: Rp{saldo:,.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")


def tambah_pengeluaran():
    global saldo, transactions
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
        if jumlah > saldo:
            print("Saldo tidak cukup")
            return
        saldo -= jumlah
        transaksi = {
            "type": "pengeluaran",
            "amount": jumlah,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        transactions.append(transaksi)
        save_data()
        print(f"Berhasil menambahkan pengeluaran sebesar Rp{jumlah:,.2f}. Saldo sekarang: Rp{saldo:,.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")


def lihat_saldo():
    print("=== Saldo Saat Ini ===")
    print(f"Saldo sekarang: Rp{saldo:,.2f}")


def laporan():
    print("=== Laporan Transaksi ===")
    total_in = sum(t.get("amount", 0) for t in transactions if t.get("type") == "pemasukan")
    total_out = sum(t.get("amount", 0) for t in transactions if t.get("type") == "pengeluaran")
    print(f"Total pemasukan : Rp{total_in:,.2f}")
    print(f"Total pengeluaran: Rp{total_out:,.2f}")
    print(f"Saldo sekarang   : Rp{saldo:,.2f}")
    print("--- Rincian transaksi ---")
    if not transactions:
        print("Belum ada transaksi.")
        return
    for i, t in enumerate(transactions, start=1):
        tipe = "Masuk" if t.get("type") == "pemasukan" else "Keluar"
        waktu = t.get("time", "-")
        amount = t.get("amount", 0)
        print(f"{i}. {waktu} - {tipe}: Rp{amount:,.2f}")


def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan")
    print("5. Keluar")


if __name__ == "__main__":
    load_data()
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
            laporan()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")