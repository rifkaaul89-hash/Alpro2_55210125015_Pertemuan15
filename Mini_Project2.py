print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Implementasi Awal Mini Project")
print("Materi: CLI System Blueprint")
print("Pertemuan 13")
print("=========================")

# =====================================
# MINI PROJECT NILAI MAHASISWA
# =====================================

NAMA_FILE = "data.txt"

# Membuat file awal jika belum ada
def buat_file_awal():
    data_awal = [
        ("A001", 80), ("A002", 75), ("A003", 90),
        ("A004", 65), ("A005", 88), ("A006", 70),
        ("A007", 95), ("A008", 60), ("A009", 78),
        ("A010", 85)
    ]

    with open(NAMA_FILE, "w") as file:
        for nim, nilai in data_awal:
            file.write(f"{nim},{nilai}\n")


# Membaca data dari file
def baca_file():
    data = {}

    try:
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                nim, nilai = baris.strip().split(",")
                data[nim] = float(nilai)

    except FileNotFoundError:
        buat_file_awal()
        return baca_file()

    return data


# Menyimpan data ke file
def simpan_file(data):
    with open(NAMA_FILE, "w") as file:
        for nim, nilai in data.items():
            file.write(f"{nim},{nilai}\n")


# Menu
def tampilkan_menu():
    print("\n===== MINI PROJECT NILAI =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Sorting Nilai")
    print("4. Cari Data")
    print("5. Edit Data")
    print("6. Hapus Data")
    print("7. Statistik")
    print("8. Simpan & Keluar")


# Tambah data
def tambah_data(data):
    nim = input("Masukkan NIM : ")

    if nim in data:
        print("NIM sudah ada.")
        return

    try:
        nilai = float(input("Masukkan Nilai : "))
        data[nim] = nilai
        print("Data berhasil ditambahkan.")

    except ValueError:
        print("Nilai harus berupa angka.")


# Tampilkan data
def tampilkan_data(data):

    if not data:
        print("Data masih kosong.")
        return

    print("\n-------------------------")
    print("No   NIM      Nilai")
    print("-------------------------")

    no = 1
    for nim, nilai in data.items():
        print(f"{no:<4} {nim:<8} {nilai}")
        no += 1

def sorting_nilai(data):

    items = list(data.items())

    for i in range(1, len(items)):

        key = items[i]
        j = i - 1

        while j >= 0 and items[j][1] > key[1]:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key

    return items

def cari_data(data):

    nim = input("Masukkan NIM : ")

    if nim in data:
        print(f"Nilai {nim} = {data[nim]}")
    else:
        print("Data tidak ditemukan.")

def edit_data(data):

    nim = input("Masukkan NIM : ")

    if nim in data:

        try:
            nilai = float(input("Masukkan nilai baru : "))
            data[nim] = nilai
            print("Data berhasil diubah.")

        except ValueError:
            print("Nilai harus angka.")

    else:
        print("Data tidak ditemukan.")

def hapus_data(data):

    nim = input("Masukkan NIM : ")

    if nim in data:
        del data[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

def statistik(data):

    if len(data) == 0:
        print("Data kosong.")
        return

    nilai = list(data.values())

    print("\n===== STATISTIK =====")
    print("Jumlah Data     :", len(nilai))
    print("Nilai Tertinggi :", max(nilai))
    print("Nilai Terendah  :", min(nilai))
    print("Rata-rata       :", round(sum(nilai) / len(nilai), 2))


# =====================================
# Program Utama
# =====================================
def main():

    data = baca_file()

    while True:

        tampilkan_menu()

        pilih = input("Pilih Menu : ")

        if pilih == "1":

            tambah_data(data)

        elif pilih == "2":

            tampilkan_data(data)

        elif pilih == "3":

            hasil = sorting_nilai(data)

            print("\nData Setelah Sorting")

            for nim, nilai in hasil:
                print(f"{nim} : {nilai}")

        elif pilih == "4":

            cari_data(data)

        elif pilih == "5":

            edit_data(data)

        elif pilih == "6":

            hapus_data(data)

        elif pilih == "7":

            statistik(data)

        elif pilih == "8":

            simpan_file(data)

            print("Data berhasil disimpan.")
            print("Program selesai.")
            break

        else:

            print("Pilihan tidak valid.")


main()

# =====================================
# Filter Nilai
# Kompleksitas : O(n)
# =====================================
def filter_nilai(data):

    try:
        batas = float(input("Tampilkan nilai >= "))

        print("\nHasil Filter")
        print("-----------------------")

        ditemukan = False

        for nim, nilai in data.items():

            if nilai >= batas:
                print(f"{nim} : {nilai}")
                ditemukan = True

        if not ditemukan:
            print("Tidak ada data.")

    except ValueError:
        print("Input harus angka.")


# =====================================
# Nilai Tertinggi
# Kompleksitas : O(n)
# =====================================
def nilai_tertinggi(data):

    if len(data) == 0:
        print("Data kosong.")
        return

    maksimum = max(data.values())

    print("\nMahasiswa dengan nilai tertinggi")

    for nim, nilai in data.items():

        if nilai == maksimum:
            print(f"{nim} : {nilai}")


# =====================================
# Nilai Terendah
# Kompleksitas : O(n)
# =====================================
def nilai_terendah(data):

    if len(data) == 0:
        print("Data kosong.")
        return

    minimum = min(data.values())

    print("\nMahasiswa dengan nilai terendah")

    for nim, nilai in data.items():

        if nilai == minimum:
            print(f"{nim} : {nilai}")
