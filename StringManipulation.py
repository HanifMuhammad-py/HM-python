print("Operasi dan Manipulasi String")

# 1.  Concatenate (Menyambung String)
nama_awal   =   "Hanif Muhammad"
nama_tengah =   "raja"
nama_akhir  =   "Python"

# (+)   untuk menggabungkan beberapa string
# ("<spasi>")  untuk menambahkan spasi pada kalimat
nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print("nama saya adalah", nama_lengkap)



# 2. Menghitung Panjang String (len)
panjang_string = len(nama_lengkap)
print (f'jumlah angka pada "{nama_lengkap}" adalah {panjang_string}')


# 3. Menghitung apakah komponen karakter tertentu pada string di string

# (in)
a = "Python"
a_in = a in nama_lengkap 
print(f'apakah ada kalimat "Python" pada {nama_lengkap} ?  {str(a_in)}')

# (not in)
a = "Python"
a_in = a not in nama_lengkap 
print(f'apakah tidak ada kalimat "Python" pada {nama_lengkap} ? {str(a_in)}')


# 4. mengulang kalimat tertentu pada string (str*x)
print("emang eak, "*10)

# 5. indexing
#    index dimulai dari 0, bukan 1
#    index juga dapat membaca spasi, dan variable lain seperti , {} ; "" dsb   
#    -1 (minis) berarti index membaca dari belakang
#    Jika ingin x - y, maka penulisannya x : y+1

print("nama_lengkap" " " "=" " " "Hanif muhammad Raja Python")
print(f"index ke-0 adalah = {nama_lengkap[0]}")
print(f"index ke-5 adalah = {nama_lengkap[5]}")
print(f"index ke-5 adalah = {nama_lengkap[6]}")
print(f"index ke-(-1) adalah = {nama_lengkap[-1]}")
print(f"index ke-0 sampai ke-5) adalah = {nama_lengkap[0:6]}")


# spasi (kecil) ------------>>>>  A (kecil)------------>>>> Z (besar)
#5. abjad paling kecil (min)
print(f"paling kecil dari : {min(nama_lengkap)}")

#6. abjad paling besar (max)
print(f"paling kecil dari : {max(nama_lengkap)}")

#7. ASCII Code

# ASCII = American Standard Code for Information Interchange — sistem penomoran yang mengubah karakter 
# -
# Kenapa perlu ASCII?
# Komputer hanya mengerti angka (0 dan 1). Jadi setiap huruf, angka, dan simbol punya kode angka 
# -masing-masing agar komputer bisa mengenalinya.

#Fungsi ord() dan chr():
#ord("A")    # → 65  (karakter ke angka)
#chr(65)     # → 'A' (angka ke karakter)

#ord("a")    # → 97
#ord("A")    # → 65
# huruf kecil selalu 32 lebih besar dari huruf kapital

ascii_code = ord(" ")
print(f"ASCII code untuk spasi adalah {str(ascii_code)}")
data = 113
print(f"char untuk ASCII 113 adalah {chr(data)}")

#8. Operator dalam bentuk method (shortcut)
data = "Hanif Muhammad Si Dewa Python"
x = data.count("a")
print(f'jumlah huruf "O" pada "{data}" = {str(x)}')

