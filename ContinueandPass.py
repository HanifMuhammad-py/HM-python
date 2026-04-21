print("Continue and Pass")

#PASS
angka = 0
while angka < 5 :
    print(f'maka angka --> {angka}')
    angka += 1

    if angka == 4 :
        pass #untuk mengisi command yang harus diisi (note u/ py bahwa kolom ini akan diisi nanti, lewati dulu ya.)
print("end!\n")


# CONTINUE
print(f'{8*"="} Without Continue {8*"="}')
angka = 0
while angka < 5 :
    print(f'maka angka --> {angka}')
    angka += 1

    if angka == 4 :
        print("stop !")
    print("loop") # akan loop di sini, kembali ke atas.)
print("end!\n")

print(f'{8*"="} With Continue {8*"="}')
angka = 0
while angka < 5 :
    print(f'maka angka --> {angka}')
    angka += 1

    if angka == 4 :
        print("stop !")
        continue # Tidak akan lanjut ke stage selanjutnya, loop kembali ke atas.)
    print("loop")
print("end!")