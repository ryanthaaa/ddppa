from Data.data import *
from Data.mahasiswa import Mahasiswa

# <=== CRUD MAHASISWA ===>

def cariMhs(dataCsvMhs, nim):
    for i in dataCsvMhs:
        if i.nim == nim:
            return i
    return None

def tambahMhs(dataCsvMhs):
    nim = nimOtomatis()
    
    print(f"NIM Mahasiswa baru : {nim}")
    nama = input("Masukan Nama : ")

    nilaiTugas = float(0)
    nilaiUts = float(0)
    nilaiUas = float(0)
    kehadiran = {}

    dataCsvMhs.append(Mahasiswa(nim, nama, nilaiTugas, nilaiUts, nilaiUas, kehadiran))
    saveDataMhs(dataCsvMhs)
    print("Data Mahasiswa Berhasil Ditambahkan!")

def lihatMhs(dataCsvMhs, nim):
    mhs = next((m for m in dataCsvMhs if m.nim == nim), None)
    if not mhs:
        print("Data tidak ditemukan!")
        return

    pkn, pks = panjangTabel([mhs])
    headerTabel(pkn, pks)
    cetakDataTabel(mhs, pkn)
    print("-" * pks)

def updateMhs(dataCsvMhs):
    nim = input("Masukan NIM : ")
    mhs = cariMhs(dataCsvMhs, nim)
    
    if not mhs:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")
        return
    
    pkn, pks = panjangTabel([mhs])
    headerTabel(pkn, pks)
    cetakDataTabel(mhs, pkn)
    print("-" * pks)

    while True:
        print("\nPilih data yang ingin diupdate")
        print("1. Nama")
        print("2. Nilai Tugas")
        print("3. Nilai UTS")
        print("4. Nilai UAS")
        print("5. Absensi")
        print("6. Kembali")

        try:
            pilih = int(input("Pilihan : "))
        except ValueError:
            print("Pilihan harus angka!")
            return
        
        if pilih == 1: mhs.nama = input("Input Nama baru : ")
        elif pilih == 2: mhs.nilaiTugas = float(input("Input Nilai Tugas baru : "))
        elif pilih == 3: mhs.nilaiUts = float(input("Input Nilai Uts baru : "))
        elif pilih == 4: mhs.nilaiUas = float(input("Input Nilai Uas baru : "))
        elif pilih == 5:
            try:
                pertemuan = int(input("Update absensi pertemuan ke- (1-16) : "))
            except ValueError:
                print("Harus angka!")
                return

            if not (1 <= pertemuan <= 16):
                print("Pertemuan tidak valid!")
                return

            lama = mhs.kehadiran.get(str(pertemuan), "-")
            print(f"Status lama : {lama}")

            while True:
                baru = input("Status baru (H/A/I/-) : ").strip().upper()
                if baru in ("H", "A", "I", "-"):
                    break
                print("Input salah!")

            mhs.kehadiran[str(pertemuan)] = baru
            break

        elif pilih == 6: return
        else: print("Pilihan Tidak Valid!"); continue

    saveDataMhs(dataCsvMhs)
    print(f"Data Mahasiswa dengan NIM {nim} Berhasil Diperbaharui!!")

def hapusMhs(dataCsvMhs):
    nim = input("Masukan NIM mahasiswa yang ingin dihapus : ")
    mhs = cariMhs(dataCsvMhs, nim)
    
    if mhs:
        dataCsvMhs.remove(mhs)
        saveDataMhs(dataCsvMhs)
        print(f"Mahasiswa dengan NIM : {nim} berhasil dihapus!!")
    else:
        print(f"Mahasiswa dengan NIM : {nim} tidak ditemukan!!")    
        
# <=== NILAI AKADEMIK ===>
    
def inputNilaiMhs(dataCsvMhs):
    nim = input("Masukan NIM : ")
    mhs = cariMhs(dataCsvMhs, nim)
    
    if not mhs:
        print("Data tidak ditemukan!!")
        return
    elif mhs.nim == nim:
        print(f"Mahasiswa dengan NIM {nim} adalah {mhs.nama}"); print()
    
    try:
        tugas = float(input("Masukan nilai Tugas (1-100) : "))
        uts   = float(input("Masukan nilai UTS   (1-100) : "))
        uas   = float(input("Masukan nilai UAS   (1-100) : "))

        if not (1 <= tugas <= 100 and 1 <= uts <= 100 and 1 <= uas <= 100):
            print("Nilai harus di antara 1-100!")
            return

        mhs.nilaiTugas = tugas
        mhs.nilaiUts   = uts
        mhs.nilaiUas   = uas

        saveDataMhs(dataCsvMhs)
        print("Nilai berhasil diinput!"); print()

    except ValueError:
        print("Input harus berupa angka!"); print()

    
# <=== PRESENSI ===>

def presensiMhs(dataCsvMhs):
    try:
        pertemuan = int(input("Masukan pertemuan ke- (1-16) : "))
    except ValueError:
        print("Harus angka!")
        return

    if not (1 <= pertemuan <= 16):
        print("Pertemuan harus 1–16")
        return

    sesi = "Praktikum" if pertemuan % 2 == 0 else "Teori"
    print(f"\n<= PERTEMUAN {pertemuan} ({sesi.upper()}) =>\n")

    for mhs in dataCsvMhs:
        # isi '-' untuk pertemuan sebelumnya jika belum ada
        for i in range(1, pertemuan):
            mhs.kehadiran.setdefault(str(i), "-")

        while True:
            status = input(f"{mhs.nama} (H/A/I/-): ").strip().upper()
            if status in ("H", "A", "I", "-"):
                break
            print("Input salah!")

        mhs.kehadiran[str(pertemuan)] = status

    saveDataMhs(dataCsvMhs)
    print("\nPresensi pertemuan berhasil disimpan.")
    
def presentasiKehadiranMhs(mhs):
    hadir = 0
    total = 0

    for status in mhs.kehadiran.values():
        if status in ("H", "A", "I"):
            total += 1
            if status == "H":
                hadir += 1

    if total == 0:
        return 0.0, 0, 0  # persen, hadir, total

    persen = (hadir / total) * 100
    return round(persen, 2), hadir, total
    
# <=== LAPORAN ===>
    
def panjangTabel(dataCsvMhs):
    if not dataCsvMhs:
        return 4, 165

    pkn = max(len(mhs.nama) for mhs in dataCsvMhs) # pkn => panjang karakter nama
    pks = 161 + pkn # pks => panjang karakter "-" / strip
    return pkn, pks

def headerTabel(pkn, pks):
    header = (f"| {'':^6} | {'':^{pkn}} | {'':^6} | {'':^6} | {'':^6} | {'':^11} | {'':^7} |")
    for i in range(1, 17):
        header += f"{str(i):^{3 if i < 10 else 4}} |"
    header += f" {'':^7} |"
                        
    print("-" * pks)
    print(f"| {'':^6} | {'':^{pkn}} | {'':^6} | {'':^6} | {'':^6} | {'':^11} | {'':^7} | {'KEHADIRAN':^85}| {'':^7} |")
    print(f"| {'NIM':^6} | {'Nama':^{pkn}} | {'Tugas':^6} | {'UTS':^6} | {'UAS':^6} | {'Nilai Akhir':^11} | {'Grade':^7} |{'-' * 86}| {'% Hadir':^7} |")
    print(header)
    print("-" * pks)

def cetakDataTabel(mhs, pkn): # pkn => panjang karakter nama    
    baris = (
        f"| {mhs.nim:^6} | "
        f"{mhs.nama:<{pkn}} | "
        f"{int(mhs.nilaiTugas):^6} | "
        f"{int(mhs.nilaiUts):^6} | "
        f"{int(mhs.nilaiUas):^6} | "
        f"{int(mhs.nilaiAkhir()):^11} | "
        f"{mhs.grade():^7} |"
    )

    for i in range(1, 17):
        status = mhs.kehadiran.get(str(i), "-")
        baris += f"{status:^{3 if i < 10 else 4}} |"
    
    persen, hadir, total = presentasiKehadiranMhs(mhs)
    baris += f" {persen:^6}% |"
            
    print(baris)

def laporanMhs(dataCsvMhs):        
    pkn, pks = panjangTabel(dataCsvMhs)
    
    print("\n# Laporan Seluruh Data Mahasiswa")
    headerTabel(pkn, pks)
    
    for i in dataCsvMhs:
        cetakDataTabel(i, pkn)
    
    if not dataCsvMhs:
        panjang = pkn + pks
        print(f"{'<=== DATA TIDAK DITEMUKAN ==>':^{panjang}}")
    
    print("-" * pks); print()