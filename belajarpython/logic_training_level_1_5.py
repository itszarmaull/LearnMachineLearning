"""
LOGIC TRAINING – LEVEL 1.5
Fokus:
- Filtering
- Chained Comparison
- Output Control
"""

print("="*55)
print("LOGIC TRAINING – LEVEL 1.5")
print("="*55)

# ======================================
# SOAL 1 — FILTER SEDERHANA
# ======================================
print("\n[SOAL 1] Filter Sederhana")

data = [4, 9, 15, 21, 30]

# rODO:
for data_no1 in data : 
    if(10 <= data_no1 <= 25):
        print(data_no1)
# Tampilkan hanya angka yang berada di antara 10 dan 25


# ======================================
# SOAL 2 — FILTER + ENUMERATE
# ======================================
print("\n[SOAL 2] Filter + Enumerate")
nilai = [45, 68, 72, 88, 90]


# tODO:
# Tampilkan output:
# Nilai dinyatakan LULUS jika ≥ 70

for i, nilaino2 in enumerate(nilai) : 
    if(nilaino2 >= 70 ) : 
        print(f'Data ke-{i+1} LULUS {nilaino2}')
# Data ke-3 LULUS (72)
# Data ke-4 LULUS (88)
# Data ke-5 LULUS (90)


# ======================================
# SOAL 3 — FILTER 2 LIST SEJAJAR
# ======================================
print("\n[SOAL 3] Filter 2 List Sejajar")

nim = ['B01', 'B02', 'B03', 'B04']
nilai = [55, 75, 60, 85]

# Nilai dinyatakan LULUS jika ≥ 70
# Tampilkan:
for i, nilaino3 in enumerate(nilai) : 
    if(nilaino3 >= 70 ) : 
        print(f'{nim[i]} -- LULUS')
# B02 - LULUS
# B04 - LULUS


# ======================================
# SOAL 4 — CHAINED COMPARISON CHECK
# ======================================
print("\n[SOAL 4] Chained Comparison Check")

angka = [5, 8, 12, 18, 25, 30]

# tODO:
# Tampilkan hanya angka yang:
# lebih besar dari 7
# dan lebih kecil dari 20
for n in angka :
    if(7<= n <=20) : 
        print(n)
print("\n=== SELESAI LEVEL 1.5 ===")
print("Fokus dikit-dikit tapi dalem 🧠🔥")
