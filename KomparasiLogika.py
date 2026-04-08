#komparasi logika 

#kenapa input "float", bisa mengeluarkan output "true" (bolean)?
#karena float digunakan untuk menyimpan angka inputan dari user. 
#-Tapi yang kamu print adalah iskurangdari, yaitu hasil dari operasi 
#-perbandingan (<). Operasi perbandingan selalu menghasilkan tipe 
#-boolean (True atau False), bukan float.

input_user = float(input("masukan angka yang bernilai kurang dari 3 dan lebih dari 10 :"))

#  ------- <3 xxxxxxxx
#memeriksa angka lebih dari 3
is_kurangdari = (input_user < 3)
print("kurang dari tiga :", is_kurangdari)


# xxxxxxx 10> -------
#memeriksa angka kurang dari 10
is_lebihdari = (input_user > 10)
print("lebih dari sepuluh :", is_lebihdari)


# ------- <3 xxxxxxxx 10> -------
#memeriksa angka kurang dari 3 dan lebih dari 10
#menggunakan logika "or", karena "kurang dari 3 atau lebih dari 10"
is_correct = is_kurangdari or is_lebihdari
print("angka yang anda masukan adalah :", is_correct)


input_user = float(input("masukan angka yang bernilai lebih dari 3 dan kurang dari 10 :"))

#  xxxxxxxx 3> ------- <10 xxxxxxxx
#memeriksa lebih dari 3 dan kurang dari 10
#menggunakan logika "and", karena "lebih dari 3 dan kurang dari 10"

is_lebihdari = (input_user >3)
print("lebih dari 3", is_lebihdari)


is_kurangdari = (input_user <10)
print("kurang dari 10", is_kurangdari)

is_correct = is_lebihdari and is_kurangdari 
print("lebih dari 3 dan kurang dari 10 :", is_correct)



##----------------------------------------------------------------------------------------------)
##----------------------------------------------------------------------------------------------)
##----------------------------------------------------------------------------------------------)
#LATIHAN KOMPARASI LOGIKA 
#Hitung (+)-nya

#NO 1
# --- 0 +++ 5 --- 8 +++ 11 ---
input_user = float(input("masukaan data >0 namun <5 dan >8 namun <11 : "))

is_lebihdari_x = (input_user >0)
is_kurangdari_x = (input_user <5)
is_lebihdari_y = (input_user >8)
is_kurangdari_y = (input_user <11)

is_x = is_lebihdari_x and is_kurangdari_x
is_y = is_lebihdari_y and is_kurangdari_y

is_correct = is_x or is_y
print("masukaan data >0 namun <5 dan >8 namun <11 :", is_correct)


#NO 2
# +++ 0 --- 5 +++ 8 --- 11 +++
input_user = float(input("masukan angka <0 dan >5 namun <8 dan >11 :"))


is_kurangdari_x = (input_user <0)
is_lebihdari_x = (input_user >5)
is_kurangdari_y = (input_user <8)
is_lebihdari_y = (input_user >11)

is_center = (is_lebihdari_x and is_kurangdari_y)

is_correct = (is_kurangdari_x or is_center or is_lebihdari_y)
print("masukan angka <0 dan >5 namun <8 dan >11", is_correct) 
