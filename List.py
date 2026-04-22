print("List []")

# List berisi Data integer
data_int = [1, 3, 5, 7, 9]
print(data_int)

# List berisi Data float
data_float = [1.1 , 3.2 , 5.3, 7.4, 9.5]
print(data_float)

# List berisi Data string
data_str = ["Several", "Oracles"]
print(data_str)

# List berisi Data boolean
data_bool = [True, False, True, True]
print(data_bool)

# Data dalam list juga bisa dicampur
data_campuran = [1, 2.3, "Several", True]
print(data_campuran)

# Cara alternatif membuat list
# start, stop, step
data_range = range (1, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comrprehension
# Start, stop, step
data_for = [i*2 for i in range (2, 10, 2)]
print(data_for)


# membuat list dengan for + if
# Start, stop, step
# if i != <variable yang akan dihilangkan/tidak dianggap>
data_for = [i*2 for i in range (2, 10, 2) if i != 4]
print(data_for)


# membuat list dengan for + if untuk bilangan genap saja
# Start, stop, step
data_for = [i for i in range (1, 10) if i%2 == 0]
print(data_for)


# membuat list dengan for + if untuk bilangan ganjil saja
# Start, stop, step
data_for = [i for i in range (1, 10) if i%2 != 0]
print(data_for)