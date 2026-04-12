print("Manipulasi String Part.2")

# Operator dalam bentuk methods
# Merubah case dari string

print("===========.upper===========")
# 1.    Merubah syntax ke Upper Case <syntax>.upper()
svor   = "several Oracles"
print(f"normal = {svor}")

svor_2 = svor.upper()
print(f"upper = {svor_2}")

print("===========.lower===========")
# 2.    Merubah syntax ke Lower Case <syntax>.lower()
svor   = "SEVERAL ORACLES"
print(f"normal = {svor}")

svor_2 = svor.lower()
print(f"lower = {svor_2}")


# Pengecekan dengan is<command> method

print("===========.isupper===========")
# 1.    pengecekan syntax ke Upper Case <syntax>.upper()
svor   = "SEVERAL ORACLES"
print(f'apakah "{svor}" tedapat upper Case? {svor.isupper()}')

svor_2 = "several oracles"
print(f'apakah "{svor_2}" tedapat upper Case? {svor_2.isupper()}')

# 2.    pengecekan syntax ke Lower Case <syntax>.lower()
svor   = "SEVERAL ORACLES"
print(f'apakah "{svor}" tedapat Lower Case? {svor.islower()}')

svor_2 = "several oracles"
print(f'apakah "{svor_2}" tedapat Lower Case? {svor_2.islower()}')


# isalpha()     ---> Untuk mengecek apakah semuanya huruf?
# isdecimal()   ---> Untuk mengecek apakah semuanya angka?
# isalnum()      ---> Untuk mengecek apakah semuanya huruf dan angka(alphanumeric)?
# isspace()     ---> Untuk mengecek apakah semuanya spasi, tab, newline (\n)?
# istitle()     ---> Untuk mengecek apakah dimulai dengan huruf kapital?


print("===========.isalpha===========")
fixera = "fixera"
print(f"apakah semuanya huruf = {fixera.isalpha()}")

print("===========.isdecimal===========")
fixera = "13122131"
print(f"apakah semuanya angka = {fixera.isdecimal()}")

print("===========.isalnum===========")
fixera = "1312fixera"
print(f"apakah semuanya alphanumeric = {fixera.isalnum()}")

print("===========.isspace===========")
fixera = "     "
print(f"apakah semuanya spasi, tab, newline = {fixera.isspace()}")

print("===========.istitle===========")
fixera = "fixera"
print(f"apakah dimulai dengan huruf kapital = {fixera.istitle()}")


# mengecek komponen apakah dimulai dari x ( startswith(<"...">) )

print("===========.startswith===========")
fixera = "fixera severaloracles"
print(f'apakah dimulai dengan "fixera" = {fixera.startswith("fixera")}')


print("===========.endswith===========")
fixera = "fixera severaloracles"
print(f'apakah diakhiri dengan "fixera" = {fixera.endswith("fixera")}')


# Pembangunan Komponen join()
print("===========.join===========")
terpisah = f"hanif muhammad", "raja", "python"
join = f"{' '.join(terpisah)}"

print(terpisah)
print(join)

# Pembangunan Komponen split()
# '<variable/kata yang ingin displit>'
print("===========.split===========")
tersambung = f"hanifmuhammadrajapython"
split = f"{(tersambung).split('raja')}"

print(tersambung)
print(split)

#r/ljust and center
#contoh rjust(<total jarak>, <dan bisa juga symbol pemisah>)
# Alokasi karakter rjust() "rata kanan"
print("===========.rjust===========")
right = f"{'kanan'.rjust(10, '=')}"
print(right)

# Alokasi karakter ljust() "rata kiri"
print("===========.ljust===========")
left = f"{'kiri'.ljust(10, '=')}"
print(left)

# Alokasi karakter center() "rata tengah"
print("===========.center===========")
center = f"{'tengah'.center(10, '=')}"
print(center)

# Alokasi karakter strip() 
# menghilangkan pinggiran pada output 
print("===========.strip===========")
strip = f"{'strip'.strip("=")}"
print(strip)
