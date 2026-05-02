data_programmer = {}  # kosong dulu

import datetime
while True:
    # input data
    key = input("Masukan ID programmer: ")
    
    data_programmer[key] = {
        "Nama"         : input("Masukan Nama: "),
        "Domisili"     : input("Masukan Domisili: "),
        "Language"     : input("Masukan Language: "),
        "Tanggal Lahir": datetime.date(
            int(input("Tahun (YYYY): ")),
            int(input("Bulan (MM): ")),
            int(input("Tanggal (DD): "))
        )
    }
    
    # tanya lanjut atau tidak
    is_done = input("Tambah data lagi? (y/n): ")
    if is_done == "n":
        break

# print tabel setelah semua input selesai
print(f'{"key":<14} {"Nama":<16} {"Domisili":<15} {"Language":<15} {"Tanggal_Lahir":<25}')
print(f'{80*"-"}')

for key in data_programmer:
    d = data_programmer[key]
    print(f'{key:<14} {d["Nama"]:<16} {d["Domisili"]:<15} {d["Language"]:<15} {str(d["Tanggal Lahir"]):<25}')