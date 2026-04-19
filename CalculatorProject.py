print("Calculator Project")
print(30*"=")

angka_pertama = float(input("masukan angka ke-1 = "))
operator = input("masukan (+ / - / x / :) = ")
angka_kedua = float(input("masukan angka ke-2 = "))

if operator==("+") :
    hasil = angka_pertama + angka_kedua  
    print(f"hasilnya adalah = {hasil} ")
elif operator==("-") :
    hasil = angka_pertama - angka_kedua
    print(f"hasilnya adalah = {hasil} ")
elif operator==("x") or operator==("*") :
    hasil = angka_pertama * angka_kedua
    print(f"hasilnya adalah = {hasil} ")
elif operator==(":") or operator==("/"):
    hasil = angka_pertama / angka_kedua
    print(f"hasilnya adalah = {hasil} ")
else : 
    print("masukan operasi aritmatika!")
print(30*"=")