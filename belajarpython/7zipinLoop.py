nim = ['001', '002', '003']
nama = ['agus', 'bejo', 'tejo']
hoby = ['berenang', 'badminton', 'football']

for d_nim, d_nama, d_hoby in zip(nim, nama, hoby) : 
    print(f'{d_nim} -- {d_nama} -- {d_hoby}')