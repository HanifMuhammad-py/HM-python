#Operasi Penjumlahan                                (+)
#Operasi Pengurangan                                (-)
#Operasi Perkalian                                  (*)
#Operasi Pembagian                                  (/)
#Operasi Eksponen (pangkat)                         (**)
#Operasi Modulus (sisa dari pembagian)              (%)
#Operasi Floor Division (pembulatan dari pembagian) (//)
#Operasi Prioritas                                  ()

# select + ctrl D = Ubah satu satu variable ke variable yang sama.)

a = 15
b = 5

hasil = a + b
print (a,"+", b,"=",hasil)

hasil = a - b
print (a, "-", b, "=", hasil)

hasil = a * b
print (a, "*", b, "=", hasil)

hasil = a / b
print (a, "/", b, "=", hasil)

hasil = a ** b
print (a, "**", b, "=", hasil)

hasil = a % b
print (a, "%", b, "=", hasil)

hasil = a // b
print (a, "//", b, "=", hasil)

#urutan untuk prioritas :
#    1.  ()
#    2.  eksponen (**)
#    3.  yang lainnya

##jika ditambahkan kurung () pada variable, maka variable tersebut akan dikerjakan duluan.
##dan pastinya akan merubah hasil penjumlahannya.

x = 3
y = 5
z = 10

hasil = x + y - z * z / y ** x
print(x, "+", y, "-", z, "*", z, "/", y, "**", x, "=", hasil)

#contoh pakai kurung ()
hasil = x + (y - z) * z / y ** x
print(x, "+", y, "-", z, "*", z, "/", y, "**", x, "=", hasil)