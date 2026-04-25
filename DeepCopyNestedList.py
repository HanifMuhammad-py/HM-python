print("Deep Copy Nested List\n")

data_1 = [4, 1]
data_2 = [2, 0]

print (f'{10*"="} Shallow .Copy() {10*"="}')
data_x = [data_1, data_2, 10]
data_x_copy =  data_x.copy()
print(f'data_x (Sebelum diubah)     = {data_x}')
print(f'data_x_copy (Sebelum diubah)= {data_x_copy}')

print (f'{50*"="}')
# .copy hanya bisa mengcopy data di dalam list[]
data_x [2] = 5
data_x [1] [0] = 3
print(f'data_x (Setelah diubah)      = {data_x}')
print(f'data_x_copy (Setelah diubah) = {data_x_copy}\n')

print(f'{10*"="} HEX ID LOCATION Shallow .copy() {10*"="}')
print(f'hex id data_x ---> {hex(id(data_x))}')
print(f'hex id data_x_copy ---> {hex(id(data_x_copy))}\n')


# Deep Copy
# bisa ganti data di luar list[]
# from copy import deep copy
# <variable> = deepcopy(<variablecopy>)

from copy import deepcopy
data_x = [data_1, data_2, 10]
data_x_deepcopy = data_x
data_x = deepcopy(data_x_deepcopy)

print (f'{10*"="} deepcopy() {10*"="}')
print(f'data_x (Sebelum diubah)         = {data_x}')
print(f'data_x_deepcopy (Sebelum diubah)= {data_x_deepcopy}\n')

data_x [2] = 7
data_x [1] [0] = 3
data_x_deepcopy = data_x
print (f'{10*"="} deepcopy() {10*"="}')
print(f'data_x (setelah diubah)         = {data_x}')
print(f'data_x_deepcopy (setelah diubah)= {data_x_deepcopy}\n')

# hex location juga 
print(f'{10*"="} HEX ID LOCATION deepcopy() {10*"="}')
print(f'hex id data_x ---> {hex(id(data_x))}')
print(f'hex id data_x_deepcopy ---> {hex(id(data_x_deepcopy))}')
