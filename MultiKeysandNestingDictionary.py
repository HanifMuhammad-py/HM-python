print ("Multi Keys and Nesting Dicitonary\n")

import datetime
# datetime.date → hanya tanggal
# datetime.date(2002, 12, 13)
# → 2002-12-13

# datetime.datetime → tanggal + waktu
# datetime.datetime(2002, 12, 13)
# → 2002-12-13 00:00:00

# datetime.datetime lengkap
# datetime.datetime(2002, 12, 13, 10, 30, 45)
# → 2002-12-13 10:30:45  (tahun, bulan, tgl, jam, menit, detik)


data_programmer1 = {
    "Nama"          : "Hanif Muhammad",
    "Domisili"      : "Jakarta",
    "Language"      : "Python",
    "Tanggal Lahir" : datetime.date(2002,12,13)
}
print(data_programmer1)


data_programmer2 = {
    "Nama"          : "nipeh saripeh",
    "Domisili"      : "Tambun selatan",
    "Language"      : "CSS",
    "Tanggal Lahir" : datetime.date(2001,1,2)
}
print(data_programmer2)


data_programmer3 = {
    "Nama"          : "Jokri Windowdow",
    "Domisili"      : "Solo",
    "Language"      : "C++",
    "Tanggal Lahir" : datetime.date(1990,5,28)
}
print(data_programmer1)


data_programmer = {
    "Programmer001" : data_programmer1,
    "Programmer002" : data_programmer2,
    "Programmer003" : data_programmer3,
}

print(data_programmer)

print(f'{"key":<14} {"Nama":<16} {"Domisili":<15} {"Language":<15} {"Tanggal_Lahir":<25}')
print(f'{80*"-"}')
for programmer in data_programmer :
    key = programmer

    Nama = data_programmer[key]["Nama"]
    Domisili = data_programmer[key]["Domisili"]
    Language = data_programmer[key]["Language"]
    Tanggal_Lahir = data_programmer[key]["Tanggal Lahir"].strftime("%x")
    print(f'{key:<15} {Nama:<15} {Domisili:<15} {Language:<15} {Tanggal_Lahir:<25}')
pass
    
