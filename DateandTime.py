print("Date and Time")

# import datetime
import datetime as dt

# today ()
today = dt.date.today()
print(today)

# date (yyyy/m/dd)
# dt.date(yyyy/m/dd) bisa mengetahui hari apa berdasarkan yyyy/m/dd yang kita masukan
tanggal = dt.date(1999,1,1)
print(tanggal)
# f-string date
print(f'hari ini tanggal = {dt.date(2026,4,18)}')
print(f'hari ini, adalah hari {today}')

# format date and time (:%X)
# x (capital) = real function
# x (huruf kecil) = mempersingkat output

# yyyy mm dd (present)
print(f'{5*"="}yyyy mm dd (present){5*"="}')
# :%A (menampilankan hari)
print(f'hari ini hari = {today:%A}')

# :%d (menampilankan tanggal)
print(f'hari ini tanggal = {today:%d}')

# :%m (menampilankan bulan(angka))
print(f'hari ini bulan = {today:%m}')

# :%B (menampilankan bulan(kata))
print(f'hari ini bulan = {today:%B}')

# :%Y (menampilankan tahun)
print(f'hari ini tahun = {today:%Y}')

#yyy mm dd (past)
print(f'{5*"="} yyy mm dd (past) {5*"="}')
tanggal_lahir_saya = dt.date(2002,12,13)
# :%A (menampilankan hari)
print(f'saya lahir hari = {tanggal_lahir_saya:%A}')

# :%d (menampilankan tanggal)
print(f'saya lahir tanggal = {tanggal_lahir_saya:%d}')

# :%m (menampilankan bulan(angka))
print(f'saya lahir bulan = {tanggal_lahir_saya:%m}')

# :%B (menampilankan bulan(kata))
print(f'saya lahir bulan = {tanggal_lahir_saya:%B}')

# :%Y (menampilankan tahun)
print(f'saya lahir tahun = {tanggal_lahir_saya:%Y}')


# yyyy mm dd (input)
print(f'{5*"="} yyyy mm dd (input) {5*"="}')
input_tanggal = (int(input("masukan tanggal lahir anda (dd)= ")))
input_bulan = (int(input("masukan bulanl lahir anda (m)= ")))
input_tahun = (int(input("masukan tahun lahir anda (yyyy)= ")))

inputX = dt.date(input_tahun, input_bulan, input_tanggal)

print(f'anda lahir hari  = {inputX:%A}')

# :%d (menampilankan tanggal)
print(f'anda lahir tanggal = {inputX:%d}')

# :%m (menampilankan bulan(angka))
print(f'anda lahir bulan = {inputX:%m}')

# :%B (menampilankan bulan(kata))
print(f'anda lahir bulan = {inputX:%B}')

# :%Y (menampilankan tahun)
print(f'anda lahir tahun = {inputX:%Y}')

# latihan
print(f'{5*"="}latihan{5*"="}')
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
