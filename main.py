import json
import time

saldo = 0
pemasukan_list = []
pengeluaran_list = []

def load_data():
    global saldo, pemasukan_list, pengeluaran_list
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            saldo = data.get('saldo', 0)
            pemasukan_list = data.get('pemasukan', [])
            pengeluaran_list = data.get('pengeluaran', [])
    except FileNotFoundError:
        pass  # File belum ada, gunakan default

def save_data():
    data = {
        'saldo': saldo,
        'pemasukan': pemasukan_list,
        'pengeluaran': pengeluaran_list
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)

load_data()

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: 💰 "))
        saldo += jumlah
        pemasukan_list.append(jumlah)
        print(f"Pemasukan sebesar {jumlah} berhasil ditambahkan! 🎉 Saldo sekarang: {saldo}")
    except ValueError:
        print("Input tidak valid. Masukkan angka saja. 😅")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: 💸 "))
        if saldo >= jumlah:
            saldo -= jumlah
            pengeluaran_list.append(jumlah)
            print(f"Pengeluaran sebesar {jumlah} berhasil! 🎉 Saldo sekarang: {saldo}")
        else:
            print(f"Saldo tidak cukup! 😟 Saldo saat ini: {saldo}")
    except ValueError:
        print("Input tidak valid. Masukkan angka saja. 😅")

def lihat_saldo():
    print("=== Saldo Anda ===")
    print(f"💰 {saldo}")

def lihat_laporan():
    total_pemasukan = sum(pemasukan_list)
    total_pengeluaran = sum(pengeluaran_list)
    print("=== Laporan Rekap ===")
    print(f"Total Pemasukan: {total_pemasukan} 💰")
    print(f"Total Pengeluaran: {total_pengeluaran} 💸")
    print(f"Saldo Saat Ini: {saldo} 💵")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. ➕ Tambah pemasukan")
    print("2. ➖ Tambah pengeluaran")
    print("3. 👀 Lihat saldo")
    print("4. 📊 Lihat laporan")
    print("5. 🚪 Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
        print("\n")
        time.sleep(2)
    elif pilihan == "2":
        tambah_pengeluaran()
        print("\n")
        time.sleep(2)
    elif pilihan == "3":
        lihat_saldo()
        print("\n")
        time.sleep(2)
    elif pilihan == "4":
        lihat_laporan()
        print("\n")
        time.sleep(2)
    elif pilihan == "5":
        save_data()
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
        print("\n")
        time.sleep(2)