#Test casting base on Tipe Data
#type data = int, float, str (string), bool (bolean)
#JANGAN LUPA SAVE SYNTAX (CTRL + S) WOYYYYYY!!!!!!!!!!!!!!!!

print ("====INTER====")
data_inter = 10

data_float = float(data_inter)
data_str = str(data_inter)
data_bool = bool(data_inter)

print ("data= ", data_inter, "type = ", int(data_inter) )
print ("data= ", data_float, "type = ", float(data_inter) )
print ("data= ", data_str, "type = ", str(data_inter) )
print ("data= ", data_bool, "type = ", bool(data_inter) )


print ("====FLOAT====")
#if decimal 9.9, bukan dibulatkan ke 10, melainkan ke 9
data_float = 10.0

data_inter = float(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print ("data= ", data_inter, "type = ", int(data_float) )
print ("data= ", data_str, "type= ", str(data_float))
print ("data= ", data_bool, "type= ", bool(data_float))


print ("====STRING====")
#int, float harus numerik, jika alphabet akan "error"
#jika, str 0 (numerik) = bool "false". Jika, str "0" (alphabet) = bool "true"
#jika, str alphabet = "true"
data_str = 0

data_inter = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

#print ("data= ", data_inter, "type = ", int(data_str) )
#print ("data= ", data_float, "type= ", float(data_str))
print ("data= ", data_bool, "type= ", bool(data_str))


print ("====BOOLEAN====")
#bolean, if false = 0, if true =/ 0
data_bool = True

data_inter = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)

print ("data= ", data_inter, "type = ", int(data_bool) )
print ("data= ", data_float, "type= ", float(data_bool))
print ("data= ", data_str, "type= ", str(data_bool))
print ("data= ", data_bool, "type= ", bool(data_bool))