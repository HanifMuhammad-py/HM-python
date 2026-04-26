print("Tuples and Set\n")

print(f'{10*"="} list [] {10*"="}')
# List []
# utak-atik (v)
# indexing (v)
data = [2, 5, 8, 4, 6]

# contoh 1
data.append(5)
print(data)

# contoh 2
print(f'index no. 6 ---> {data[-1]}\n')


print(f'{10*"="} Tuples () {10*"="}')
# Tuples ()
# utak-atik (x)
# indexing (x)

data = (2, 5, 8, 4, 6)
 
# contoh 1
data.append(5)
print(data)

# contoh 2
print(f'index no. 6 ---> {data[-1]}\n')


print(f'{10*"="} set {10*"="}')
# set {} / himpunan
# utak-atik (v)
# bisa menambahkan data tapi pakai <variable>.add()
# indexing (x)
data = {2, 5, 8, 4, 6}
 
# contoh 1
data.append(5)
print(data)

# contoh 2
print(f'index no. 6 ---> {data[-1]}\n')
