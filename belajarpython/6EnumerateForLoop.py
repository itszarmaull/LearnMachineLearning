# cara konvensional 
nim = ['001', '002', '003']
nama = ['agus', 'bejo', 'tejo']
for i in range(len(nim)) : 
    print(f'{nim[i]} -- {nama[i]}')

# VERSI PYTHONIC
print('Versi Pythonic : ')
nim = ['004', '005', '006']
nama = ['fazar', 'fais', 'fariz']
for i, data_nim in enumerate(nim) :
    print(f'{data_nim} -- {nim[i]}')