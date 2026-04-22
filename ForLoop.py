print("For Loop")

# [] = list (kumpulan data)
# i = kumpulang data-data di dalam []
# for kondisi : 
#   aksi

# basic {i} on loop
angka =  [0, 2, 4, 6, 8, 10]
print(f"{10*'='} i for loop {10*'='}")
for i in angka :
    print(f'i on --> {i}')
print("Terima Kasih !\n")

# Range start {i} on loop
angka =   range (5)
print(f"{10*'='} i on loop {10*'='}")
for i in angka :
    print(f'i on --> {i}')
print("Terima Kasih !\n")

# Range (start, stop) {i} on loop
angka =  range (2,6)
print(f"{10*'='} i on loop {10*'='}")
for i in angka :
    print(f'i on --> {i}')
print("Terima Kasih !\n")

# Range (start, stop, step) {i} on loop
# step = lompatan dari angka ke angka lainnya
angka =  range (0, 12, 2)
print(f"{10*'='} i on loop {10*'='}")
for i in angka :
    print(f'i on --> {i}')
print("Terima Kasih !\n")