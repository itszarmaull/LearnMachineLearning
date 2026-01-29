"""
QUIZ LOGIC PYTHONIC
Materi:
1. Swapping Value
2. Chained Comparison
3. Packing Nilai
4. Unpacking Nilai
5. For Loop Pythonic
6. Enumerate For Loop

RULES:
- Jangan pakai solusi konvensional
- Utamakan gaya pythonic
- Jangan lihat jawaban dulu 
"""

print("="*50)
print("QUIZ LOGIC PYTHONIC")
print("="*50)

# ======================================
# SOAL 1 — SWAPPING VALUE
# ======================================
print("\n[SOAL 1] Swapping Value")

x = 5
y = 9

print(f"Sebelum: x={x}, y={y}")

# TODO: Tukar nilai x dan y (tanpa variabel tambahan)
x,y = y,x
print(f"Sesudah: x={x}, y={y}")


# ======================================
# SOAL 2 — CHAINED COMPARISON
# ======================================
print("\n[SOAL 2] Chained Comparison")

nilai = 76

#todo
# Cetak "Lulus" jika nilai di antara 70 dan 85
print(70<= nilai >= 85)
# Cetak "Tidak Lulus" jika tidak memenuhi


# ======================================
# SOAL 3 — PACKING SEKUMPULAN NILAI
# ======================================
print("\n[SOAL 3] Packing Nilai")

a = 2
b = 4
c = 6

# TODO:
# Masukkan a, b, c ke dalam satu list bernama data
data = [a,b,c]

print("Data:", data)


# ======================================
# SOAL 4 — UNPACKING SEKUMPULAN NILAI
# ======================================
print("\n[SOAL 4] Unpacking Nilai")

data2 = [100, 200, 300]

# todo
# Ambil isi data2 ke variabel x, y, z
x,y,z = data2

print(f"x={x}, y={y}, z={z}")


# ======================================
# SOAL 5 — FOR LOOP PYTHONIC
# ======================================
print("\n[SOAL 5] For Loop Pythonic")

buah = ['apel', 'jeruk', 'mangga']

#tODO:
# Tampilkan semua isi list tanpa range() dan len()

for item in buah : 
    print(f'{item}')
# ======================================
# SOAL 6 — ENUMERATE FOR LOOP
# ======================================
print("\n[SOAL 6] Enumerate For Loop")

nama = ['andi', 'budi', 'citra']

# tODO:
# Tampilkan output:
# 1. andi
# 2. budi
# 3. citra
# (gunakan enumerate)
for i, nama_data in enumerate(nama) :
    print(f'{i+1}.{nama_data} ')


print("\n=== SELESAI ===")
print("Kalau sudah, kirim kodenya ke gue buat dicek 💪🔥")
