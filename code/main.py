from Data.data import loadDataMhs
import Data.proses as proses

dataCsvMhs = loadDataMhs()

def menuAwal():
    print("\n<========== PROJECT ==========>")
    print("1. Manajemen Data Mahasiswa")
    print("2. Nilai Akademik")
    print("3. Presensi")
    print("4. Laporan")
    print("5. Exit")

    try:
        pil = int(input("Masukan Pilihan : ").strip())
    except ValueError:
        print("Input harus angka!")
        return menuAwal() # Itulah 4 trio

    if pil == 1:
        return menuManajemen()
    elif pil == 2:
        proses.inputNilaiMhs(dataCsvMhs)
    elif pil == 3:
        proses.presensiMhs(dataCsvMhs)
    elif pil == 4:
        proses.laporanMhs(dataCsvMhs)
    elif pil == 5:
        print("Program Selesai...")
        return
    else:
        print("Pilihan tidak tersedia!")

    return menuAwal() # Itulah 4 trio

def menuManajemen():
    print("\n<========== MANAJEMEN MAHASISWA ==========>")
    print("1. Tambah Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Update Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Kembali")

    try:
        pil = int(input("Masukan Pilihan : ").strip())
    except ValueError:
        print("Input harus angka!")
        return menuManajemen() # Itulah 4 trio

    if pil == 1:
        proses.tambahMhs(dataCsvMhs)
    elif pil == 2:
        nim = input("Cari Mahasiswa dengan NIM : ")
        proses.lihatMhs(dataCsvMhs, nim)
    elif pil == 3:
        proses.updateMhs(dataCsvMhs)
    elif pil == 4:
        proses.hapusMhs(dataCsvMhs)
    elif pil == 5:
        return menuAwal()
    else:
        print("Pilihan tidak tersedia!")

    return menuManajemen() # Itulah 4 trio

menuAwal()