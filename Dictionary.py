print("Dictionary\n")

# Normal dat
data = ["Hanif", "raja", "python"]
print(data[2])

# Dictionary (dict) =  
# <variable {}
# identifier : key
# how to print ? print(<variable>[variable dict])

data_dict = {
    "x"     : "1312", 
    "y"     : "Several",
    "z"     : "Oracles",
    "fx"    : [13, 12, 2],
    "svor"  : 1312 
}
print(f'{data_dict["x"]}{data_dict["fx"]}')
print(f'{data_dict["y"]} {data_dict["z"]}')
print(f'data pada dict svor --> {data_dict["svor"]}')