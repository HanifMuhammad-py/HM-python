print(f'{"Package":^30}')
print(f'{"="*30}')

# file to file = import only
# bisa import <folder>.<file>
# bisa juga from <folder> import <file>
# file __pychace__ u/ membuat import dieksekusi dengan cepat oleh computer
import packageTESTING


hasil_tambah = packageTESTING.tambah(3)
print(f'Hasil tambah = {hasil_tambah}')

hasil_pangkat = packageTESTING.pangkat(2)
print (f'Hasil pangkat = {hasil_pangkat}')


# folder to file = 
import maintest

hasil_bagi = maintest.bagi (20)
print (f'Hasil Bagi = {hasil_bagi}')