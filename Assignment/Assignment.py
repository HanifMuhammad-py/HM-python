#operasi Assignment
# operasi ditambah / dieskponen menggunakan suatu assignment.
#a = 2, a += 5 (nilai a + 5) = 7, a -= 2 (nilai a yg terbaru dikurang 2) = 5.

#contoh assignment untuk operasi aritmatika, modulus, floor division dan eksponen
print("\ncontoh assignment untuk operasi aritmatika, modulus, floor division dan eksponen")
a = 7
print("nilai a =", a)

print("\n========  +  ========")
a += 5
print ("a += 5  (nilai a + 5)")
print("nilai a menjadi :", a)

print("\n========  -  ========")
a -= 5
print ("a -= 5 (nilai a - 5)")
print("nilai a menjadi :", a)

print("\n========  *  ========")
a *= 5
print ("a *= 5 (nilai a * 5)")
print("nilai a menjadi :", a)

print("\n========  /  ========")
a /= 5
print ("a /= 5 (nilai a / 5)")
print("nilai a menjadi :", a)

print("\n========  %  ========")
a %= 5
print ("a %= 5 (nilai a % 5)")
print("nilai a menjadi :", a)

print("\n========  //  ========")
a //= 5
print ("a //= 5 (nilai a // 5)")
print("nilai a menjadi :", a)

print("\n========  **  ========")
a **= 5
print ("a **= 5 (nilai a ** 5)")
print("nilai a menjadi :", a)


print("\nhasilnya sama saja dengan :" )
#sama saja dengan
a = 7
print("#sama saja dengan") 
hasil = (a + 5 - 5) * 5 / 5 % 5 // 5 ** 5
print(a, "+", 5, "-", 5, "*", 5, "/", 5, "%", 5, "//", 5, "**", "=", hasil)

# contoh penerapan assignment untuk operasi bitwise (or, and, xor, not)
print("contoh penerapan assignment untuk operasi bitwise (or, and, xor, not)")

b = True

#or (|)
#logic yg dipakai, ketika ada 1 atau lebih variable bernilai "true", 
print("\n========  or (|)  ========")
b = True
print("nilai b =", b)
b |= True #(b = true or true)
print(" nilai b |= true, maka nilai b =", b)
b = True
print("nilai b =", b)
b |= False #(b = true or false)
print(" nilai b |= false, maka nilai b =", b)


#and (&)
#JIKA ADA "FALSE" MAKA HASIL AKAN FALSE.
print("\n========  or (&)  ========")
b = True 
print("nilai b =", b)
b &= True #(b = true and true)
print(" nilai b &= true, maka nilai b =", b)
b = True
print("nilai b =", b)
b &= False #(b = true and false)
print(" nilai b &= false, maka nilai b =", b)



#xor (^)
#JIKA ADA YANG SAMA MAKA FALSE.
print("\n========  xor (^)  ========")
b = True
print("nilai b =", b)
b ^= True #(b = true xor true)
print(" nilai b ^= true, maka nilai b =", b)
b = True
print("nilai b =", b)
b ^= False #(b = true xor false)
print(" nilai b ^= false, maka nilai b =", b)


#shift command

#shift right
print("\n========  shift right (>>)  ========")
d = 0b0100
print("nilai d:",d, format(d,"04b"))
d >>= 0b0100
print("nilai d:",d, format(d,"04b"))


#shift left
print("\n========  shift left (<<)  ========")
d = 0b0100
print("nilai d:",d, format(d,"04b"))
d <<= 0b0100
print("nilai d:",d, format(d,"04b"))