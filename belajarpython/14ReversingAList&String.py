# CARA KONVENSIONAL 
angka1 = [10,20,30,40,50,60]
# angka2 = []

# for i in range(len(angka1)) : 
#     reverse_i = len(angka1) -1 -i
#     angka2.append(angka1[reverse_i])
# print(f'angka 1 : {angka1}')
# print(f'angka 2 : {angka2}')

# cara pythonic 
angka2  = angka1[::-1]
print(f'angka ke 2 : {angka2}')
