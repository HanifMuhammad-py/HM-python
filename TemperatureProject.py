#menghitung perhitungan sederhana
# \n.......\n = untuk memperpadat/merapihkan output pada terminal



print("\nProgram konverensi Temperatur\n")

celcius = float(input("suhu dalam satuan celcius : "))
print("satuan celcius adalah : ", celcius, "celcius")

reamur = (4/5) * celcius
print("satuan dalam reamur adalah : ", reamur, "reamur")

fahrenheit = (9/5) * celcius + 32
print("satuan dalam fahrenheit adalah : ", fahrenheit, "fahrenheit")

kelvin  = celcius + 273
print("satuan dalam kelvin adalah : ", kelvin, "kelvin")


#latihan

print("\nfahrenheit ke kelvin\n")
fahrenheit  = float(input("masukan suhu dalam farenheit :"))
celcius     = ((5/9) * fahrenheit) + 32
kelvin      = celcius +  273 
print("suhu kelvinnya adalah :", kelvin, "kelvin")


print("\nkelvin ke fahrenheit\n")
kelvin      = float(input("masukan suhu dalam kelvin :"))
celcius     = kelvin - 273
fahrenheit  = ((9/5) * celcius) + 32
print("suhu fahrenheitnya adalah :", fahrenheit, "fahrenheit")