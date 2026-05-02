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

    Tahun_lahir = int(input("Masukan Tahun (YYYY) : "))
    Bulan_lahir = int(input("Masukan Bulan (1/12) : "))
    Tanggal_lahir = int(input("Masukan Tanggal (1-31) : "))
    programmer["Tanggal Lahir"] = datetime.date(Tahun_lahir, Bulan_lahir, Tanggal_lahir)

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

    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    # kita akan bikin key dengan random variable, dan memilihi string (ascii_uppercase) dan dibuat sebanyak 6
    # kita bikin random untuk setiap {i} di dalam range 6
    data_programmer.update({key:programmer})

    print(f'{"key":<14} {"Nama":<16} {"Domisili":<15} {"Language":<15} {"Tanggal_Lahir":<25}')
    print(f'{80*"-"}')


    for programmer in data_programmer :
        key = programmer

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
    