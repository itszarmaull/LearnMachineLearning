"""
LOGIC TRAINING – LEVEL 2
Fokus:
- map + lambda
- filter logic
- zip
- enumerate
- chained comparison
- data flow mindset (mirip preprocessing ML)
"""

print("="*65)
print("LOGIC TRAINING – LEVEL 2")
print("="*65)

# ======================================
# SOAL 1 — NORMALISASI DATA
# ======================================
print("\n[SOAL 1] Normalisasi Data")

nilai = [50, 60, 70, 80, 90]

#tTODO:
nilai_normalisasi = list(map(lambda x : x/100, nilai))
print(f'nilai awal : {nilai}')
print(f'nilai normalisasi : {nilai_normalisasi}')
# Ubah semua nilai menjadi skala 0–1
# (hint: nilai / 100)
# Gunakan map + lambda


# ======================================
# SOAL 2 — FILTER & TRANSFORM
# ======================================
print("\n[SOAL 2] Filter & Transform")

data = [3, 7, 12, 18, 25, 40]

# tODO:
# 1. Ambil hanya angka di antara 10 dan 30
filteredData = []
for item in data : 
    if(10 < item < 30) : 
        filteredData.append(item)
# 2. Kalikan hasilnya dengan 3
print(f'filter : {filteredData}')
hasil = list(map(lambda x : x*3, filteredData))
print(f'hasil X*3 : {hasil}')
# Gunakan filter + map (alur jelas)


# ======================================
# SOAL 3 — ZIP DATASET (FEATURE + LABEL)
# ======================================
print("\n[SOAL 3] Zip Dataset")

nama = ['andi', 'budi', 'citra', 'doni']
nilai = [65, 82, 90, 55]

# Aturan:
# LULUS jika nilai >= 70
for d_nama, d_nilai in zip(nama, nilai) : 
    if(d_nilai >= 70) : 
        print(f'{d_nama} - LULUS')
# tODO:
# Tampilkan hanya:
# budi - LULUS
# citra - LULUS


# ======================================
# SOAL 4 — ENUMERATE + FILTER
# ======================================
print("\n[SOAL 4] Enumerate + Filter")

nilai = [45, 72, 88, 60, 95]
print(f'nilai awal : {nilai}')
# to
# Tampilkan hanya nilai LULUS
for i, data_nilai in enumerate(nilai) : 
    if(data_nilai >= 70) : 
        print(f'Data ke-{i+1} - LULUS {data_nilai}')
# Format:
# Data ke-2 LULUS (72)
# Data ke-3 LULUS (88)
# Data ke-5 LULUS (95)


# ======================================
# SOAL 5 — CHAINED COMPARISON (CLEANING)
# ======================================
print("\n[SOAL 5] Data Cleaning")

sensor = [2, 8, 15, 22, 30, 35]

# tODO:
# Anggap data valid jika:
filtersensor = [];
for item in sensor : 
    if(5 < item < 30) : 
        filtersensor.append(item)
print(f'data valid : {filtersensor}')
# lebih besar dari 5
# dan lebih kecil dari 30
# Tampilkan hanya data valid


# ======================================
# SOAL 6 — STRING TRANSFORM (MAP)
# ======================================
print("\n[SOAL 6] String Transform")

kategori = ['ml', 'ai', 'dl', 'cv']

# tODO:
nama_kapital = list(map(lambda x : x.upper(), kategori))
print(nama_kapital)
# Ubah semua kategori menjadi format:
# ML, AI, DL, CV
# Gunakan map + lambda


print("\n=== SELESAI LEVEL 2 ===")
print("Pelan tapi konsisten = naik kelas 🧠🔥")
