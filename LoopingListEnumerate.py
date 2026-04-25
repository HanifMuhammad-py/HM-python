print("Looping List enumerate")


print("\nFor Loop")
# for loop
# hanya Looping sederhana tanpa indexing
data_x = [1, 6, 5, 2, 3, 2 ]
for data in data_x :
    print(f'angka = {data}')
pass


print("\nFor [i] on range loop")
# for [i] loop on range
# looping dengan indexing dan (Start, Stop, Step)
for i in range (1,len(data_x), 2) :
    print(f'angka = {data_x[i]}')
pass


print("\nList Comprehension")
# List Comprehension
# agak lucu sih, print di dalam list[]
# [print(f'string{variable})for <variable> in <variable datalist>]

[print(f'angka= {i}')for i in data_x] 

# mengubah variable {i}
[print(f'angka= {i**3}')for i in data_x] 


print("\nList Comprehension")
# enumerate
# mendapatkan loop, data, dan index location
# for <index>,<varibalelist> in enumerate(variable)
#       print({variablelist})

for index, data in enumerate(data_x) :
    print(f'angka = {data}') 
pass