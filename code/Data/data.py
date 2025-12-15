import csv, json
from Data.mahasiswa import Mahasiswa

def loadDataMhs():
    dataMhs = []
    
    with open("Data/data.csv", "r", newline="") as file:
        data = csv.reader(file)
        next(data)
        
        for i in data:
            kehadiran = json.loads(i[5]) if i[5] else {}
            dataMhs.append(Mahasiswa(i[0], i[1], i[2], i[3], i[4], kehadiran))
    
    return dataMhs

def saveDataMhs(dataMahasiswa):
    with open("Data/data.csv", "w", newline="") as file:
        dataBaru = csv.writer(file)
        
        dataBaru.writerow(["nim", "nama", "nilai_tugas", "nilai_uts", "nilai_uas", "kehadiran"])

        for i in dataMahasiswa:
            dataBaru.writerow([i.nim, i.nama, i.nilaiTugas, i.nilaiUts, i.nilaiUas, json.dumps(i.kehadiran)])
            
def nimOtomatis():
    with open("Data/data.csv", "r", newline="") as file:
        ngambilNim = csv.reader(file)
        next(ngambilNim)

        Nim = []

        for i in ngambilNim:
            if i:
                Nim.append(int(i[0]))
                
        if not Nim:
            return "0001"

        nimBesar = max(Nim) + 1
        return str(nimBesar).zfill(4)