import csv

class Mahasiswa:
    def __init__(self, nim, nama, nilaiTugas = 0, nilaiUts = 0, nilaiUas = 0, kehadiran = None):
        self.nim = nim
        self.nama = nama
        self.nilaiTugas = float(nilaiTugas)
        self.nilaiUts = float(nilaiUts)
        self.nilaiUas = float(nilaiUas)
        self.kehadiran = kehadiran if kehadiran is not None else {}
        
    def nilaiAkhir(self):
        nilaiAkhir = lambda tugas, uts, uas: (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        return nilaiAkhir(self.nilaiTugas, self.nilaiUts, self.nilaiUas)
    
    def grade(self):
        nilaiAkhir = self.nilaiAkhir()
        if nilaiAkhir >= 80: return "A"
        elif nilaiAkhir >= 70: return "B"
        elif nilaiAkhir >= 55: return "C"
        elif nilaiAkhir >= 40: return "D"
        else: return "E"
                