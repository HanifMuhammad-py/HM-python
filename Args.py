print(f'{"*ARGS":^80}')
print(f'{"="*40:^80}\n')

# *args (args) bisa diganti dengan variable apapun (non int)
# ex : *data, *format, *dll

'''basic *args'''
def function (nama, umur, domisili) :
    print(f'"Nama = "{nama}')
    print(f'"Umur = "{umur}')
    print(f'"Domisili = "{domisili}')
    
    return function

function("hanif", 18, "Jakarta")

print(f'{"="*40}')

'''list def'''
def function_1 (data) :
    nama        = data[0]
    umur        = data[1]
    domisili    = data[2]
    print(f'"Nama = "{nama}')
    print(f'"Umur = "{umur}')
    print(f'"Domisili = "{domisili}')

    return function_1 

# U/ list, jika tanpa argument *args, return wajib menggunakan [] 
function_1(["hanif", 18, "Jakarta"])

print(f'{"="*40}')

'''list def w/ *args'''
def function_2 (*args) :
    nama        = args[0]
    umur        = args[1]
    domisili    = args[2]
    print(f'"Nama = "{nama}')
    print(f'"Umur = "{umur}')
    print(f'"Domisili = "{domisili}')

    return function_2 

function_2("hanif", 18, "Jakarta")

print(f'{"="*40}')

'''math w/ *args'''
# data dengan type = tuple, jadi bisa di iterasi
def function_3 (*data) :
    output = 1
    for angka in data :
        output *= angka 
    return output

result = function_3(1, 3, 5, 6)
print(f'Hasil = {result}')





