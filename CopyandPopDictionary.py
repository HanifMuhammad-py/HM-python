print("Copy and Pop Dictionary")

data_dict = {
    "x" : "integer",
    "y" : "float",
    "z" : "string",
    "a" : "bollean",
}
print(f'{7*'='} = (NON COPY) {7*'='}') 
# = (non .copy())
data_dict_x = data_dict
print(data_dict_x)

# ubah data
data_dict["x"] = "int"
data_dict["a"] = "boolean"

# hasil with = (non copy)
print(f'data dict: {data_dict}')
print(f'data dict_x: {data_dict_x}')

print(f'data_dict --> {hex(id(data_dict))}')
print(f'data_dict_x --> {hex(id(data_dict_x))}')

print (16*"=")
data_dict_2 = {
    "x" : "integer",
    "y" : "float",
    "z" : "string",
    "a" : "bollean",
}

print(f'{7*'='} .COPY() {7*'='}')
# <Variable> = <variable dict>.copy()
data_dict_copy = data_dict_2.copy()
print(data_dict_copy) 

# ubah data
data_dict_2["x"] = "int"
data_dict_2["a"] = "boolean"

# hasil with .copy()
print(f'data dict: {data_dict_2}')
print(f'data dict_copy: {data_dict_copy}')

print(f'data_dict_2 --> {hex(id(data_dict_2))}')
print(f'data_dict_copy --> {hex(id(data_dict_copy))}')


# Pop
# untuk memidahkan data values dari satu variable ke variable lain
# <variable baru> = <variable dictionary>.pop(<key yang mau dipindah>)

data_pop = data_dict.pop("a")
print(f'variable baru, data pop --> {data_pop}')
print(f'data_dict --> {data_dict}')

# Pop Item
# untuk memidahkan data key + values yang terakhir dari satu variable ke variable lain
#<variable baru> = <variable dictionary>.pop(<key yang mau dipindah>)
data_pop = data_dict.popitem()
print(f'variable baru, data pop --> {data_pop}')
print(f'data_dict --> {data_dict}')


# gunakan .append agar data tidak tertimpa saat proses pemindahan ke-2 dst...
data_pop = []
data_pop.append(data_pop("a"))
data_pop.append(data_pop.popitem())

print(data_pop)