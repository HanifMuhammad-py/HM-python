print("Operation List\n")

data_dict = {
    "x" : "integer",
    "y" : "float",
    "z" : "string",
    "a" : "bollean",
}

# Mengetahui banyaknya data dalam dict
len_data = len(data_dict)
print(len_data)

# mengecek key exist
# variable x = variable yg mau dicheck
# variable = variable x in variable dict
# output = boolea
key = 'x'
check = key in data_dict
print(check)

# mengecek values #1 exist dengan values()
# if <dict data> in variables.values()
# output = if else
if "float" in data_dict.values() :
    print("True")
else :
    print("False")
pass

# mengecek key = 
# variable = (variable dict.get())
data_get = (data_dict.get("x"))
print(data_get)

# update data

# mengubah data
# <variable>[key] = values
data_dict["x"] = "int"
print(data_dict) 

# menambah data
# <variable>[key] = values
data_dict["b"] = "loop"
print(data_dict)

# update data key and values
# jika ada key yang exist maka update akan mengubah data yang sudah ada
# jika data key belum exist maka akan menambah data yang sudah ada
# <variable>.update({key : values})
data_dict.update({"x":"integer"})
print(data_dict)

data_dict.update({"c":"bitwise"})
print(data_dict)

# delete data pada dict
# del <variable dict>["key"]
del data_dict["b"]
print(data_dict)
