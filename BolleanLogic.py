#operasi logika atau boolean
#not, or, and, xor

# not (~)
#KEBALIKAN DATA AWAL
print("======not======")

a = True
b = not a

print("data a =", a)

print("=====not=====")
print("data b =", b)

# or (|)
#JIKA ADA "TRUE" MAKA HASIL AKAN TRUE.
#logic yg dipakai, ketika ada 1 atau lebih variable bernilai "true", 
#-maka hasil logika boolean akan true.
#analogi seperti pertambahan (+)
#true 1, false 0, maka = 1 + 0 = 1 (true)
print("======or======")

a = True
b = False
x = a or b
print("function 1", "=", x)

a = True
b = True
x = a or b
print("function 2", "=", x)

a = False
b = True
x = a or b
print("function 3", "=", x)

a = False
b = False
x = a or b
print("function 4", "=", x)

#and (&)
#JIKA ADA "FALSE" MAKA HASIL AKAN FALSE.
#logic yg dipakai adalah, logic boolean akan true, jika semua variable bernilai "true".
# analogi seperti perkalian (*)
#true = 1, false = 0, maka 1 * 0 = 0
print("======and======")

a = True
b = False
x = a and b
print("function 1", "=", x)

a = True
b = True
x = a and b
print("function 2", "=", x)

a = False
b = True
x = a and b
print("function 3", "=", x)

a = False
b = False
x = a and b
print("function 4", "=", x)



#XOR (^)
#JIKA ADA YANG SAMA MAKA FALSE.
#logic yg dipakai adalah, Jika ada "wajib hanya ada 1 "true", maka hasilnya akan true.

print("======XOR======")

a = True
b = False
x = a ^ b
print("function 1", "=", x)

a = True
b = True
x = a ^ b
print("function 2", "=", x)

a = False
b = True
x = a ^ b
print("function 3", "=", x)

a = False
b = False
x = a ^ b
print("function 4", "=", x)
