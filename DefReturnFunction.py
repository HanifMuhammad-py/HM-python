print("Return Function\n")
# return = panggil variable / fungsi sebagai nilai


print(f'{10*"="} CONTOH 1 {10*"="}')
def function_x() :
    a = 5
    b = 7
    c = a + b
    return c
pass
function_1 = function_x() + 5
print(f'{function_1}\n')


print(f'{10*"="} CONTOH 2 {10*"="}')
def kuadrat(x) :
    output = x**2
    return output
pass
y = kuadrat(3)
print(y)
print(kuadrat(7))

print(f'{10*"="} CONTOH 4 {10*"="}')
# menambahkan operasi di luar function
z = kuadrat(10) ** 2
print(f'{z}\n')


print(f'{10*"="} CONTOH 5 {10*"="}')
# Return dengan multi-input
def input_x(angka_1, angka_2, angka_3) :
    return(angka_1 + angka_2 + angka_3)
pass

print(f'{input_x(10, 5, 7)}\n')


print(f'{10*"="} CONTOH 6 {10*"="}')
# return dengan multi output
def input_angka(angka_1, angka_2) :
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return(tambah, kurang, kali, bagi)

a, b ,c ,d = input_angka(5,5)
print(f'tambah = {a}')
print(f'kurang = {b}')
print(f'kali = {c}')
print(f'bagi = {d}')
