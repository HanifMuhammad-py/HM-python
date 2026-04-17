print("width and alignment")

data_nama = "Hanif Muhammad"
data_umur = 23
data_domisili = "Jakarta"
data_tinggi = 175.5

#string standard
data_string = f'nama = {data_nama} | umur = {data_umur} | domisili = {data_domisili} | tinggi badan = {data_tinggi}'
print(5*"="+"string"+"="*5)
print(data_string)

#string multiline - newline(\n)
data_string = f'nama = {data_nama} \numur = {data_umur} \ndomisili = {data_domisili} \ntinggi badan = {data_tinggi}'
print(5*"="+"string multiline"+"="*5)
print(data_string)


#string multiline - triplet("""")
data_string = f"""nama = {data_nama} 
umur = {data_umur}
domisili = {data_domisili}
tinggi badan ={data_tinggi}
"""

print(5*"="+"string triplet"+"="*5)
print(data_string)

#mengatur jarak 
data_string = f"""
nama            ={data_nama:>20} 
umur            ={data_umur:>20}
domisili        ={data_domisili:>20}
tinggi badan    ={data_tinggi:>20}
"""

print(5*"="+"mengatur jarak"+"="*5)
print(data_string)
