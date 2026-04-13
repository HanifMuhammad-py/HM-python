print("f_string")

#  huruf    nama                contoh  
#   f       float               500.00
#   d       integer             500 
#   e       notasi ilmiah       5e+02
#   %       percent             50.00%
#   ,       pemisah ribuan      1,000.000

# string
SVOR = "Several Oracles"
f_string = f"string = {SVOR}"
print(f_string)

# boolean
bool = True
f_string = f"boolean = {bool}"
print(f_string)

# angka
jumlah = 51256.00
f_string = f"jumlah = {jumlah}"
print(f_string)


# bilangan koma
# meng-koma kan bilangan 
# <variable>:, 

bilangan_koma = 1513521535
f_string = f"bilangan koma = {bilangan_koma:,}"
print(f_string)

# bilangan desimal
# menyederhanakan desimal (belakang koma / titik) 
# <variable>:.<jumlah desimal yang mau dipertahankan>f 

bilangan_desimal = 151.21535
f_string = f"bilangan desimal = {bilangan_desimal:.3f}"
print(f_string)


# bilangan leading zero
# mempertankan variable dari depan dan menambahkan 0 dari depan
# <variable>:<jumlah desimal yang mau dipertahankan dari depan + 0>
# .<jumlah desimal yang mau dipertahankan>f 

bilangan_leading_zero = 151.21535
f_string = f"bilangan leading zero = {bilangan_leading_zero:09.3f}"
print(f_string)

# menampilkan tanda + dan -
# <variable>:+d
 
angka_plus = +13
angka_minus = -13

plus = f"angka plus = {angka_plus:+d}"
minus = f"angka minus = {angka_minus:+d}"

print(plus)
print(minus)

# format percent
# mmembuat desimal menjadi percent dan mempertahankan ,.0   
# <variable>:<banyaknya variable yang ingin dpertahankan dibelakang .,>%
format_percent = 0.1312
f_string = f"format_percent = {format_percent:.3%}"
print(f_string)

# melakukan operasi aritmatika di dalam place order {}
# fungsi f dibelakang .<variable> = memberitahu python variable ini adalah angka biasa, bukan notasi ilmiah.
harga = 5000
discount = 10
f_string = f"operasi aritmatika di dalam place order = Rp{harga/discount:.0f}"
print(f_string)

# format angka lainn (binary, octal, hexadecimal)

angka = 1312
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)
