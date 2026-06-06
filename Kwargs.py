print(f'{"**KWARGS":^80}')
print(f'{"="*40:^80}\n')

# **Kwars = key word arguments
# variable = kwargs [keyword]

'''Basic **Kwargs'''
def function (**kwargs) :
    Nama        = kwargs["nama"]
    Umur        = kwargs["umur"]
    Domisili    = kwargs["domisili"]
    print(kwargs["nama"])
    print(kwargs["umur"])
    print(kwargs["domisili"])

function(nama = "hanif", umur = 18, domisili = "Tangsel")

print("="*40)

'''math w/ *Args**Kwargs'''
def function (*args,**kwargs) :
    output = 1
    if kwargs["operation"] == "tambah" :
        print("Penjumlahan")
        for angka in args :
            output += angka
    elif kwargs["operation"] == "kurang" :
        print("Pengurangan")
        for angka in args :
            output -= angka
    elif kwargs["operation"] == "kali" :
        print("Perkalian")
        for angka in args :
            output *= angka
    elif kwargs["operation"] == "bagi" :
        print("Pembagian")
        for angka in args :
            output /= angka
    return output

result = function (1, 2, 3, 4, operation = "tambah")
print(f'Hasil Penjumlahan = {result}\n') 
result = function (1, 2, 3, 4, operation = "kurang")
print(f'Hasil Pengurangan = {result}\n') 
result = function (1, 2, 3, 4, operation = "kali")
print(f'Hasil Perkalian = {result}\n')
result = function (1, 2, 3, 4, operation = "bagi")
print(f'Hasil Pembagian = {result}\n')