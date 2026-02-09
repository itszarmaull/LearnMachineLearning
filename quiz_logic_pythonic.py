"""
LOGIC TRAINING – LEVEL 1
Fokus:
- Chained Comparison
- For Loop Pythonic
- Enumerate
- Packing & Unpacking
- Mindset logika (bukan hafalan)
"""

print("="*55)
print("LOGIC TRAINING – LEVEL 1")
print("="*55)

# ======================================
# SOAL 1 — RANGE LOGIC (WARM UP)
# ======================================
print("\n[SOAL 1] Range Logic")

angka = 12

# tODO:
if(10 <= angka <=20) :
    print('Aman')
else :
    print("Bahaya")
# Cetak "AMAN" jika angka di antara 10 dan 20
# Cetak "BAHAYA" jika di luar rentang


# ======================================
# SOAL 2 — FILTER DATA (LOGIC DATA)
# ======================================
print("\n[SOAL 2] Filter Data")

data = [3, 7, 12, 18, 25, 30]

#tODO:
# Tampilkan HANYA angka yang berada di antara 10 dan 25
for i, data_loop in enumerate (data) : 
    if(10<= data_loop <= 25) : 
        print(data_loop)
# (gunakan for loop pythonic)


# ======================================
# SOAL 3 — ENUMERATE + LOGIC
# ======================================
print("\n[SOAL 3] Enumerate + Logic")

nilai = [55, 72, 81, 90, 66]

#tODO:
# Tampilkan hanya nilai yang LULUS
# Syarat lulus: nilai >= 70
for i, data_nilai in enumerate(nilai) : 
    if(data_nilai >= 70 ) : 
        print(f'Data Ke-{i+1} LULUS {data_nilai}')
    else :
        print(f'Data Ke-{i+1}, TIDAK LULUS {data_nilai}')
# Format output:
# Data ke-2 LULUS (72)
# Data ke-3 LULUS (81)
# dst...


# ======================================
# SOAL 4 — PACKING & UNPACKING LOGIC
# ======================================
print("\n[SOAL 4] Packing & Unpacking")

x = 1
y = 2
z = 3

# tODO:
# 1. Packing x, y, z ke dalam list
list = [x,y,z]
print(f'Packing ke list : {list} ')
# 2. Unpack kembali ke variabel a, b, c
a,b,c = list;
# 3. Cetak hasilnya
print('Unpacking : ')
print(f'a={a}, b={b}, c={c}')


# ======================================
# SOAL 5 — RELASI 2 LIST (LOGIC SEJAJAR)
# ======================================
print("\n[SOAL 5] Relasi 2 List")

nim = ['A01', 'A02', 'A03', 'A04']
nilai = [65, 80, 45, 90]

# tODO:
# Tampilkan:
for i, n in enumerate(nilai) : 
    if(n >=70) : 
        print(f'{nim[i]} -- LULUS')
    else : 
        print(f'{nim[i]} -- Tidak Lulus ')
# A02 - LULUS
# A04 - LULUS
# (nilai >= 70)


# ======================================
# SOAL 6 — MINDSET ERROR CHECKING
# ======================================
print("\n[SOAL 6] Error Checking")

angka_list = [5, 10, 15, 20, 25]

# tODO:
# Tampilkan hanya angka yang:
for item in angka_list : 
    if(22 <= item >= 8) :
        print(item) 
# - lebih besar dari 8
# - lebih kecil dari 22


print("\n=== SELESAI LEVEL 1 ===")
print("Pelan tapi konsisten = ML engineer mindset 🧠🔥")
