print("Copy List")

# Pass by References
# variable 1 akan = variable 2 (meskipun salah satu diganti, variable lain akan mengikuti)
# memiliki hex location yang sama

a =  ["Hanif", "si", "raja", "python"]
print(a)

b = a
print(b)

# hex location
hex_a = hex(id(a))
hex_b = hex(id(b))

print(f'hex location a = {hex_a}')
print(f'hex location b = {hex_b}')


# Copy List
# bagaimana jika ingin  menduplikat suatu variable[], namun variable 1 tidak ikut berubah ketika variable 2 diubah
# <variable 1>.<variable 2>.copy()

c = a.copy()
print(a)
print(c)

# ubah data dari variable 2 != ubah data variable 1
c[2] = "king" 
print(a)
print(c)

# Hex Location
# Hex location memiliki lokasi yang berbeda, sehingga a != c
hex_a = hex(id(a))
hex_c = hex(id(c))

print(f'hex location a = {hex_a}')
print(f'hex location c = {hex_c}')
