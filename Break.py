print("break")

angka = 0

while angka < 8 :
    angka += 2 
    print(f'angka sekarang --> {angka}')
    
    if angka == 6 :
        print("enough")
        break

print("end!\n")

print(f'{7*"="} COUNTDOWN {7*"="}')
data = int(input("hitung sampai angka = "))

angka = 0

while True:
    angka += 1
    print(f'Count --> {angka}')

    if angka == data :
        print("end")
        break
pass