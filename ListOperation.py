print("List Operation")

data = [0, 2, 0, 6, 5, 1, 6, 0, 6, 2, 9, 6, 2, 9, 6, 2, 9]

# menghitung banyaknya suatu data dalam sebuah list
# <variable>.count(<datanya>)
data_angka_6 = data.count(6)
print(f'jumlah data "angka 6" dalam list adalah = {data_angka_6}')

data = ["Several", "Oracles", "SAAS", "Automation", "and", "Solution"]

# mengetahui index location dalam sebuah list
# <variable>.index(<datanya>)
data_SAAS = data.index("SAAS") 
print(data_SAAS)

# mengurutkan data dari berdasarkan abjad
# <variable>.short()
data.sort()
print(data)

# reverse data dari command sebelumnya
# <variable>.reverse()
data.reverse()
print(data)