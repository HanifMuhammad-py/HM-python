print("Default Argument Function\n")
# def function(argument = nilai default)
# def

# fungsi contoh 1
def testing(nama = "hanif") :
    print (f'halo! = {nama}')
pass

testing() 

# function contoh 2
# jika saat memanggil data(), argument 1, dan argument 2 kosong --> argument 2 akan pakai default(pesan = apa kabar?)
def data(nama, pesan = 'apa kabar?') :
    print(f'hallo! {nama}, {pesan} ')
pass

data("fixera", "gimana hari ini?") # --> argument 1-2 diisi
data("hanif") # --> argument 2 kosong --> pakai default (pesan =)


# fungsi contoh 3
def aritmatika(angka_1, angka_2 = 2) :
    hasil = angka_1**angka_2
    return hasil
pass

# return wajib pakai print(def(argument))
print(aritmatika(5,5)) # --> argument 1-2 diisi
print(aritmatika(5)) # --> argument 2 kosong --> pakai default (angka_2 =)

# def function juga bisa dipanggil di luar def itu sendiri
# dalam kasus ini terbaca pangkat pada variable 1 dan 2
hasil_x = aritmatika(angka_1=7, angka_2=3)
print(hasil_x)


# fungsi contoh 4
def data_data(data_1 = 8, data_2 = 16, data_3 = 32, data_4 = 64, data_5 = 128, data_6 = 256, data_7 = 512, data_8 =1028) :
    hasil_data = data_1 + data_2 - data_3 * data_4 / data_5 ** data_6 // data_7 % data_8
    return hasil_data
pass

print(data_data()) # --> Pakai def default argument
print(data_data(data_1 = 100)) # --> bisa megubah salah satu variable dalam argument
