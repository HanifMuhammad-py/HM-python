print("Looping Dictionary\n")

data_dict = {
    "x" : "integer",
    "y" : "float",
    "z" : "string",
    "a" : "bollean",
}

# Looping first try = output interables key
for data in data_dict :
    print(f'key --> {data}\n')
pass


# Operator mengambil item / iterables
# variable = variable dict.keys()
print(f'{7*"="} INTERABLES KEYS {7*"="}') 
keys = data_dict.keys()
print(f'{keys}\n')


# variable dict.get(variable) = mengeluarkan output interables values
print(f'{7*"="}  INTERABLES VALUES 1 {7*"="}')
for key in data_dict :
    print(f'{data_dict.get(key)}\n')
pass

# atau bisa juga menggunakanan values() = mengeluarkan output interables values
# variable = variable dict.values()
print(f'{7*"="} INTERABLES VALUES 2 {7*"="}')
values = data_dict.values()
print(F'{values}\n')

print(f'{7*"="} LOOPING INTERABLES VALUES {7*"="}')
for value in data_dict :
    print(f'{data_dict.values()}\n')
pass


# mengambil key + values
# variable = variable dict.items()
print(f'{7*"="} INTERABLES ITEMS {7*"="}')
items = data_dict.items()
print(f'{items}\n')

# Looping items
print(f'{7*"="} LOOPING NTERABLES ITEMS {7*"="}')
for key, values in data_dict.items() :
    print(f'key --> {key} = values --> {values}')
