print("Dictionary Project\n")

import os
os.system("cls")
# library python > cls (windows)
# merapihkan output terminal

import random
# py library u/ menambahkan variable random

import string
# string module itu basically shortcut kumpulan karakter, isinya antara lain:
# Attribute                     isi
# Isistring.ascii_uppercase     A-Z
# string.ascii_lowercase        a-z
# string.ascii_letters          a-z + A-Z
# string.digits                 0-9
# string.punctuation            !"#$%&'()*+,...


import datetime
data_programmer1 = {
    "Nama"          : "Hanif Muhammad",
    "Domisili"      : "Jakarta",
    "Language"      : "Python",
    "Tanggal Lahir" : datetime.date(2002,12,13)
}

data_programmer = {}

while True :

    os.system("cls")
    print(f'{"SELAMAT DATANG":^20}')
    print(f'{"DATA PROGRAGMMER":^20}')
    print("-"*20)

    # membuat dictionary baru (dict) dari (.fromkeys) --> (keys yang dimaksud.keys())
    programmer = dict.fromkeys(data_programmer1.keys())

    programmer["Nama"] = input("Masukan Nama : ")
    programmer["Domisili"] = input("Masukan Domisili : ")
    programmer["Language"] = input("Masukan Languange : ")

    programmer["Tanggal Lahir"] = datetime.date(
            int(input("Tahun (YYYY): ")),
            int(input("Bulan (1-12): ")),
            int(input("Tanggal (1-31): ")),
        )
    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    # kita akan bikin key dengan random variable, dan memilihi string (ascii_uppercase) dan dibuat sebanyak 6
    # kita bikin random untuk setiap {i} di dalam range 6
    data_programmer.update({key:programmer})

    print(f'{"key":<14} {"Nama":<16} {"Domisili":<15} {"Language":<15} {"Tanggal_Lahir":<25}')
    print(f'{80*"-"}')


    for programmer_x in data_programmer :
        key = programmer_x

        Nama = data_programmer[key]["Nama"]
        Domisili = data_programmer[key]["Domisili"]
        Language = data_programmer[key]["Language"]
        Tanggal_Lahir = data_programmer[key]["Tanggal Lahir"].strftime("%x")
        
        print(f'{key:<14} {Nama:<16} {Domisili:<15} {Language:<15} {Tanggal_Lahir:<25}')
    print("\n")
    is_done = input("Lanjutkan Pengisian data? (y/n)")
    if is_done == "n" :
        break
print("Data telah tersimpan! terima kasih.")
    