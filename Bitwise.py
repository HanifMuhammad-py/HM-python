#Operator Bitwise (operasi biner, binary)

a = 7
b = 3

#bitwise OR (|)
#logic yg dipakai, ketika ada 1 atau lebih variable bernilai "true", 
#-maka hasil logika boolean akan true.
#true 1, false 0, maka = 1 + 0 = 1 (true)

C = a | b
print ("=============or============")

print("nilai :",a, ", binary :", format(a,"08b"))
print("nilai :",b, ", binary :", format(b,"08b"))
print ("------------------------------------------(|)")
print("nilai :",C, ", binary :", format(C,"08b"))


#bitwise AND (&)
#JIKA ADA "FALSE" MAKA HASIL AKAN FALSE.
#logic yg dipakai adalah, logic boolean akan true, jika semua variable bernilai "true".
#true = 1, false = 0, maka 1 * 0 = 0

C = a & b
print ("=============and============")

print("nilai :",a, ", binary :", format(a,"08b"))
print("nilai :",b, ", binary :", format(b,"08b"))
print ("------------------------------------------(&)")
print("nilai :",C, ", binary :", format(C,"08b"))


#bitwise XOR (^)
#JIKA ADA YANG SAMA MAKA FALSE.
#logic yg dipakai adalah, Jika ada "wajib hanya ada 1 "true", maka hasilnya akan true.

C = a ^ b
print ("=============xor============")

print("nilai :",a, ", binary :", format(a,"08b"))
print("nilai :",b, ", binary :", format(b,"08b"))
print ("------------------------------------------(^)")
print("nilai :",C, ", binary :", format(C,"08b"))


#bitwise NOT (~)
#dihitung dari 0. Misal, nilai yang dihitung (X) Maka hasil akan -X(+1)
#namun misal nilai yang dihitung (-X), maka hasil akan (+X)
# ----((X)+1))-------0-------(X)--
# ----(-X)-------0-------(+X)----

C = ~b
print ("=============not============")

print("nilai :",a, ", binary :", format(a,"08b"))
print ("------------------------------------------(~)")
print("nilai :",C, ", binary :", format(C,"08b"))



#bitwise Shift right (>>)
# mengurangi kode/bilangan biner ke belakang

C = a >>2  #(Contoh mengurangi 2 digit)
print ("=============shift right============")

print("nilai :",a, ", binary :", format(a,"08b"))
print ("------------------------------------------(>>)")
print("nilai :",C, ", binary :", format(C,"08b"))


#bitwise Shift left (<<)
# menambahkan kode/bilangan biner ke depan

C = a <<2  #(Contoh menambah 2 digit)
print ("=============shift left============")

print("nilai :",a, ", binary :", format(a,"08b"))
print ("------------------------------------------(<<)")
print("nilai :",C, ", binary :", format(C,"08b"))

#cara manual input bilangan / kode = bitwise /biner
print("\n#cara manual input bilangan / kode = bitwise /biner")
d = 0b01000
print("nilai d:",d, format(d,"06b"))
