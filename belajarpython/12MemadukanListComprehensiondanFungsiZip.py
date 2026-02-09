# CARA KONVENSIONAL 

# nama = ['bejo', 'karti', 'tejo']
# usia = [23,31,26]
# listku = []
# for i in range(len(nama)) : 
#     listku.append([nama[i], usia[i]])
# print(f'listku : {listku}')

# CARA PYTHONIC 
nama = ['bejo', 'karti', 'tejo']
usia = [23,31,26]
listku = [[d_nama, d_usia] for d_nama, d_usia in zip(nama, usia)]
print(f'listku {listku}')
