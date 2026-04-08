#INPUT DATA USER
#TYPE = untuk memasukan data integer / float / string / boolean.
data = input("masukan nama :")


#data yang diinput pasti data_string (str)
print ("data; ", data, "type; ",type(data))


#ubah data_string menjadi data_inter (numerik)
data_int = int(input("masukan umur :"))
print ("data; ", data_int, "type; ",type(data_int))


#kemudian coba tambahkan opsi minimal DP
angka = float(input("masukan minimal DP pembayaran :"))
print("data; ", angka, "type; ", type(angka))


#jika, menggunakan data_boolean (bool), untuk verifikasi nominal pembayaran DP maka :
#apapun inputnya, output dari terminal boolean akan "true"
#jadi, masukan / ubah dulu ke data_integer (int) agar bisa "true" / "false".
biner = bool(int(input("masukan nilai pembayaran :")))
print("data; ", biner, "type; ", type(biner))