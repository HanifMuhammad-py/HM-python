input_tanggal   = int(input("masukan tanggal lahir = "))
input_bulan     = int(input("masukan bulan lahir   = "))
input_tahun     = int(input("masukan tahun lahir   = "))

import datetime as dt
input_data = dt.date(input_tahun, input_bulan, input_tanggal)

hari_ini = dt.date.today()

umur_data = hari_ini - input_data
tahun_data = umur_data.days // 365
bulan_data = (umur_data.days % 365)  // 30
print(f'{tahun_data} tahun {bulan_data} bulan')

