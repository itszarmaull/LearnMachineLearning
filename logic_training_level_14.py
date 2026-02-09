"""
LOGIC TRAINING – LEVEL 3
Materi:
- List Comprehension + IF
- List Comprehension + ZIP
- Slicing List & String
- Reversing List & String
"""

print("="*65)
print("LOGIC TRAINING – LEVEL 3")
print("="*65)

# ======================================
# SOAL 1 — LIST COMPREHENSION + IF
# ======================================
print("\n[SOAL 1] List Comprehension + IF")

data = [5, 12, 18, 25, 30, 40]

# ODO:
# Buat list baru berisi angka yang
data2 = [item for item in data if 10 < item <30]
print(f'data 1 : {data}')
print(f'data2 : {data2}')
# - lebih besar dari 10
# - lebih kecil dari 30
# Gunakan list comprehension


# ======================================
# SOAL 2 — LIST COMPREHENSION + TRANSFORM
# ======================================
print("\n[SOAL 2] List Comprehension + Transform")

angka = [1, 2, 3, 4, 5]

# DO:
# Buat list baru berisi:
# kuadrat dari setiap angka
angka2 = [item * item  for item in angka ]
print(f'angka : {angka}')
print(f'angka2 : {angka2}')
# Gunakan list comprehension


# ======================================
# SOAL 3 — LIST COMPREHENSION + ZIP
# ======================================
print("\n[SOAL 3] List Comprehension + ZIP")

nama = ['andi', 'budi', 'citra']
usia = [19, 25, 17]

# T\ODO:
# Gabungkan nama dan usia menjadi list seperti:
# ['budi', 25]
# HANYA untuk usia >= 20
listku = [[d_nama, d_usia] for d_nama, d_usia in zip(nama, usia) if d_usia >= 20]
print(listku)
# Gunakan list comprehension + zip


# ======================================
# SOAL 4 — SLICING LIST
# ======================================
print("\n[SOAL 4] Slicing List")

listmu = [10, 20, 30, 40, 50, 60, 70]

# TODO:
# Ambil:
# - tiga elemen pertama
# - tiga elemen terakhir
awal = listmu[:3]
akhir = listmu[-3:]
# listku = [awal, akhir]
print(awal)
print(akhir)
# Gunakan slicing


# ======================================
# SOAL 5 — SLICING STRING
# ======================================
print("\n[SOAL 5] Slicing String")

kata = "PEMBELAJARANPYTHON"

# TODO:
# Ambil substring:
# - "BELAJAR"
# - "PYTHON"
belajar = kata[3:10]
python = kata[12:]
print(python)
print(belajar)
# Gunakan slicing


# ======================================
# SOAL 6 — REVERSING LIST
# ======================================
print("\n[SOAL 6] Reversing List")

angka = [10, 20, 30, 40, 50]

# TODO:
# Balik urutan list menggunakan cara pythonic
angka2 = angka[::-1]
print(angka2)
# ======================================
# SOAL 7 — REVERSING STRING
# ======================================
print("\n[SOAL 7] Reversing String")

teks = "PYTHONIC"

# TODO:
teks2 = teks[::-1]
print(teks2)
# Balik urutan string menggunakan slicing


print("\n=== SELESAI LEVEL 3 ===")
print("Kalau bisa ini, fondasi Pythonic lu SOLID 🧠🔥")
