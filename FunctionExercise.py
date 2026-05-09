print ("Function Exercise\n")

# # Header
# print(f'{"Program Perhitungan Sederhana":^50}')
# print(f'{"Menghitung Luas dan Keliling Persegi Panjang":^50}')
# print(f'{"="*50:^50}')

# # input
# lebar = int(input("Masukan nilai lebar : "))
# panjang = int(input("Masukan nilai Panjang : "))

# # Formula
# luas = lebar*panjang
# keliling = 2*(lebar+panjang)

# # Output
# print(f'luas Persegi adalah = {luas}')
# print(f'Keliling Persegi adalah = {keliling}')

# with def function() :
def header() :
    '''header'''
    print(f'{"Program Perhitungan Sederhana":^50}')
    print(f'{"Menghitung Luas dan Keliling Persegi Panjang":^50}')
    print(f'{"="*50:^50}\n')
pass

def nilai_input() :
    '''input'''
    lebar = int(input("Masukan lebar Persegi Panjang: "))
    panjang = int(input("Masukan Keliling Persegi Panjang : "))

    return lebar,panjang
pass

def formula() :
    luas = lebar*panjang
    keliling = 2*(lebar+panjang)
    
    return luas,keliling
pass


while True :
    header()
    
    lebar,panjang = nilai_input()
    luas,keliling = formula()
    print(f'Luas Dari Persegi Panjang Adalah = {luas} ')
    print(f'Keliling Dari Persegi Panjang Adalah = {keliling}')
    
    iscorrect = input("\napakah ingin lanjut ? (y/n)")
    if iscorrect == "n" :
        break
print("Akhir Dari Program, Terima Kasih!")



