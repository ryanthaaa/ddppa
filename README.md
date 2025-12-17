# 🔥DDPPA🔥
🌟 DDPPA : Dasar Dasar Pemrograman Project Akhir 
👥 By : Riantha Pratama (42530033) and Dika Gus Septa (42530015)

Sistem Informasi Akademik Mahasiswa berbasis **Command Line Interface (CLI)** yang dibangun menggunakan bahasa pemrograman **Python**.  

Program ini dirancang untuk mengelola data mahasiswa secara terstruktur, mencakup **manajemen data mahasiswa, nilai akademik, presensi, dan laporan**, dengan pendekatan **pemrograman modular dan berorientasi objek**.

---

## ✨ Fitur Utama

### 1️⃣ Manajemen Data Mahasiswa (CRUD)
- Tambah data mahasiswa dengan NIM otomatis
- Cari data mahasiswa berdasarkan NIM
- Update data mahasiswa (nama, nilai, dan absensi)
- Hapus data mahasiswa
- Validasi data agar tidak terjadi kesalahan input

### 2️⃣ Nilai Akademik
- Input nilai Tugas, UTS, dan UAS
- Validasi rentang nilai (1–100)
- Perhitungan **Nilai Akhir** menggunakan *Lambda Function*
- Penentuan **Grade otomatis** berdasarkan nilai akhir

### 3️⃣ Presensi Mahasiswa
- Presensi hingga **16 pertemuan**
- Penentuan jenis pertemuan:
  - Ganjil → **Teori**
  - Genap → **Praktikum**
- Status kehadiran:
  - `H` → Hadir
  - `A` → Alpha
  - `I` → Izin
  - `-` → Belum diisi
- Perhitungan **persentase kehadiran mahasiswa**

### 4️⃣ Laporan Akademik
- Menampilkan seluruh data mahasiswa dalam bentuk tabel
- Menampilkan:
  - NIM & Nama
  - Nilai Tugas, UTS, UAS
  - Nilai Akhir & Grade
  - Rekap kehadiran 1–16
  - Persentase kehadiran
- Tabel dinamis menyesuaikan panjang nama mahasiswa

### 5️⃣ Penyimpanan Data
- Data disimpan dalam file **CSV**
- Data tetap ada meskipun program ditutup
- Program dapat membuka kembali data yang telah disimpan

---

## 🧠 Konsep & Teknik yang Digunakan

- **Object Oriented Programming (OOP)**
- **Modular Programming**
- **Lambda Function**
- **Recursive Function (Menu Program)**
- **Validasi Input**
- **String Formatting & Dynamic Table**
- **File Handling (CSV)**

---

## 🗂 Struktur Folder

📦 Project/
│
├── Data/
│   ├── data.csv
│   ├── data.py
│   ├── mahasiswa.py
│   └── proses.py
│
└── menu.py