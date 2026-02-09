# CARA KONVENSIONAL 
# listmu = [10,20,30,40,50]
# listku = []
# for item in listmu : 
#     if item > 25 : 
#         listku.append(item)

# print (f'lismu : {listmu}')
# print (f'listku : {listku}')

# CARA PYTHONIC 
listmu = [10,20,30,40,50]
listku = [item for item in listmu if item > 25 ]
print(f'listmu : {listmu}')
print(f'listku : {listku}')
