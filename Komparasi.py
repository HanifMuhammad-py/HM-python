#operasi Komparasi
#setiap hasil dari komparasi adalah data bollean (Bool)

#jenis-jenis data komparasi :

# SYTNTAX LITERAL
# A = 4. Angka 4 nya literal, tidak bisa dipanggil lagi di kolom berikutnya =
#        tidak memakan memory.

#>          (Lebih besar)          
#<          (Lebih kecil) 
#>=         (Lebih besar sama dengan)
#<=         (Lebih kecil sama dengan) 
#==         (sama dengan)
#!=         (tidak sama dengan)
    
a = 5
b = 7

print("====== Lebih Besar ======")

Hasil = a > 6
print(a, ">", 6, "=", Hasil)

Hasil = b > 6
print(b, ">", 6, "=", Hasil)


print("====== Lebih kecil ======")

Hasil = a < 6
print(a, "<", 6, "=", Hasil)

Hasil = b < 6
print(b, "<", 6, "=", Hasil)


print("====== Lebih besar sama dengan====")
Hasil = a >= 6
print(a, ">=", 6, "=", Hasil)

Hasil = b >= 6
print(b, ">=", 6, "=", Hasil)


print("==== Lebih kecil sama dengan =====")
Hasil = a <= 6
print(a, "<=", 6, "=", Hasil)

Hasil = b <= 6
print(b, "<=", 6, "=", Hasil)


print("====== sama dengan ======")
Hasil = a == 6
print(a, "==", 6, "=", Hasil)

Hasil = b == 6
print(b, "==", 6, "=", Hasil)


print("====== tidak sama dengan ======")
Hasil = a != 6
print(a, "!=", 6, "=", Hasil)
Hasil = b != 6
print(b, "!=", 6, "=", Hasil)




# A = 4. Huruf A nya Non-literal, bisa dipanggil lagi di kolom berbeda
#        = memakan memory internal.


#a = [1,2,3]
#b = [1,2,3]

#a == b  # ✅ True  → nilainya sama
#a is b  # ❌ False → alamat memorinya BEDA (objek berbeda)

#hex(id(x))
#  └──┘
#  id(x)  → mengambil ALAMAT MEMORI objek x (dalam bentuk integer)
#  hex()  → mengubah integer tersebut ke format HEXADECIMAL

#Output contoh: 0x7ffd641b54f8 → ini adalah alamat RAM tempat variabel x disimpan, 
#               -ditampilkan dalam format hex.

#🔑 Gunanya: Untuk membuktikan apakah dua variabel menunjuk ke lokasi memori yang
#            -sama atau berbeda.


#type (x) >>> <class 'int'>
#OBJECT IDENTIFTY >>> hex (id(x))

#ini adalah assignment dalam membuat object

#is         (komparasi object identity)
x = 5 
y = 5
print("nilai x adalah", x,",","id-nya adalah", hex(id(x)))
print("nilai y adalah", y,",","id-nya adalah", hex(id(y)))
#karena variable menyimpan data yang sama, maka lokasi hex(id)
#-nya juga sama.

hasil = x is y
print("jadi hasil dari x is y", "=", hasil)


#is not.    (komparasi object identity)
x = 5 
y = 3
print("nilai x adalah", x,",","id-nya adalah", hex(id(x)))
print("nilai y adalah", y,",","id-nya adalah", hex(id(y)))
#nah pada kasus ini, karena nilai data dari variable berbeda, 
#-maka hex(id) menyimpan memory di lokasi yang berbeda juga.

hasil = x is not y
print("jadi hasil dari x is y", "=", hasil)