print("Dictionary Exercise 1\n")

# library python > cls (windows)
# merapihkan output terminal
import os
os.system("cls")


import datetime
data_programmer1 = {
    "Nama"          : "Hanif Muhammad",
    "Domisili"      : "Jakarta",
    "Language"      : "Python",
    "Tanggal Lahir" : datetime.date(2002,12,13)
}

# data_input = {}
# print(f'{data_input}\n')

print(f'{"SELAMAT DATANG":^20}')
print(f'{"DATA PROGRAGMMER":^20}')
print("-"*20)

# membuat dictionary baru (dict) dari (.fromkeys) --> (keys yang dimaksud.keys())
programmer = dict.fromkeys(data_programmer1.keys())

programmer["Nama"] = input("Masukan Nama :")
programmer["Domisili"] = input("Masukan Domisili :")
programmer["Language"] = input("Masukan Languange :")

Tahun_lahir = int(input("Masukan Tahun (YYYY) :"))
Bulan_lahir = int(input("Masukan Bulan (MM) :"))
Tanggal_lahir = int(input("Masukan Tanggal (D) :"))
programmer["Tanggal Lahir"] = datetime.date(Tahun_lahir, Bulan_lahir, Tanggal_lahir)

print(programmer)
