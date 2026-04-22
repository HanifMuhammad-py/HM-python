print ("List Manipualation")

#urutan index :      0 / -8   1 / -7    2 / -6    3/ -5     4 / -4     5 / -3    6 / -2      7 / -1
data =              ["Hanif", "raja", "python",   "dan",   "CEO",   "dari", "Several", "Oracles"]

# index data dari depan
print(f'{7*"="} Index Data Dari depan {7*"="}\n')
print(f'index 0 berisi --> {data[0]}')
print(f'index 1 berisi --> {data[1]}')
print(f'index 2 berisi --> {data[2]}')
print(f'index 3 berisi --> {data[3]}')
print(f'index 4 berisi --> {data[4]}')
print(f'index 5 berisi --> {data[5]}')
print(f'index 6 berisi --> {data[6]}')
print(f'index 7 berisi --> {data[7]}')

# index data dari belakang
print(f'{7*"="} Index Data Dari Belakang {7*"="}\n')
print(f'index -1 berisi --> {data[-1]}')
print(f'index -2 berisi --> {data[-2]}')
print(f'index -3 berisi --> {data[-3]}')
print(f'index -4 berisi --> {data[-4]}')
print(f'index -5 berisi --> {data[-5]}')
print(f'index -6 berisi --> {data[-6]}')
print(f'index -7 berisi --> {data[-7]}')
print(f'index -8 berisi --> {data[-8]}\n')

# menambahkan item pada list sesuai posisi
# <variable>.insert(<posisi index>, "list baru")
data.insert(1, "muhammad")
print(f' .insert() -->{data}\n')

# Menambahkan item di akhir list
# <variable>.append("list baru")
data.append("(SVOR)")
print(f' .append() -->{data}\n')

# Menambahkan list pada list sebelumnya
# <variable>.extend(<variable list yang baru>0)
data_baru = (True, True, False, 13, 12)
data.extend(data_baru)
print(f' .extend() -->{data}\n')

# mengubah data pada list 
# <variable>[posisi index yg mau diubah] = <data baru>
data[2] = "King"
print(f'data[] = ""-->{data}\n')

# Me-remove data pada list
# <variable>.remove(data yang baru)
# akan ERROR jika Typo
data.remove("muhammad")
print(f' .remove() -->{data}\n')

# me-remove data paling belakang
# <variable>.pop()
data.pop()
print(f' .pop() -->{data}\n')

# di .pop(), kita jg bisa melihat data terakhir di dalam sebuah list
# <variable> = <variable>.pop()
data = data.pop()
print(f'check last data w/ .pop()  --> {data}\n')


# mengetahui banyaknya jumlah data dalam suatu list []
# menggunakan len()
# len() membuat data yg tadinya str menjadi int (PERHATIKAN !!!)
data = (1, 3, 1, 2, "S", "V", "O", "R", True, False )
data = len(data)
print (f'jumlah variable dalam list "data" adalah = {data}')