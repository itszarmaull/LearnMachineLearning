print(f'Cara Manual\n ===========')

listku = [10,20,30]

def lipat_ganda(x) : 
    return x *2;

listmu = []
for item in listku : 
    listmu.append(lipat_ganda(item))

print(f'Listku =  {listku}')
print(f'Listmu = {listmu}')

print(f'Cara MAP ')
listmu = list(map(lipat_ganda, listku))
print(f'Listku =  {listku}')
print(f'Listmu = {listmu}')
