print("Latihan Perulangan")

# latihan perulangan membuat segitiga

# Perulangan menggunakan cara manual
print(f'{7*"="} Dengan Manual {7*"="}')
print ("*")
print ("**")
print ("***")
print ("****")
print ("*****")
print("\n")

# Perulangan menggunakan for
# menggunakan START, STOP, STEP
print(f'{7*"="} Dengan for i range {7*"="}')

colomn = 5
for i in range(1, colomn+1) :
    print("*"*i)
pass

print("\n")
# print yang ganjil saja
# menggunakan START, STOP, STEP

print(f'{7*"="} Print Yang Ganji saja {7*"="}')
colomn = 5
for i in range(1, colomn+1, 2) :
    print("*"*i)
pass


print("\n")
# buat output menjadi segitiga sama-kaki
# menggunakan .center + f{string} + rjust

print(f'{7*"="} buat menjadi segitiga sama-kaki {7*"="}')

colomn = 10
for i in range(1, colomn+1, 2) :
    print(f'{"*"*i:^{colomn*1}}')
pass




print("\n")
# Perulangan menggunakan while
print(f'{7*"="} Dengan while {7*"="}')
colomn = 5


start_from = 1
count = 5
while True :
    print("*"*start_from)
    start_from += 1

    if   start_from > count :
        break
print("\n")


# membuat bentuk ketupat
print(f'{7*"="} membuat bentuk ketupat {7*"="}')
x = 11

for i in range (1, x+1, 2) :
    print(f"{'*'*i:^{x}}")


for i in range (x-2, 0, -2) :
    print(f"{'*'*i:^{x}}")
print("\n")


# membuat bentuk jam pasir
# (start, stop, step)
# stop = menghilangkan variable/agka tersebut / tidak dianggap
#   jadi, harus x x(stop) + <variable penyeimbang>
print(f'{7*"="} membuat bentuk jam pasir {7*"="}')
x = 9

for i in range (9, 1, -2) :
    print(f'{"x"*i:^{x}}')

for i in range (1, 11, 2) :
    print(f'{"x"*i:^{x}}')
