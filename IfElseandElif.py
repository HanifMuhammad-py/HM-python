print("if, else and elif Statement")

# if statement 
# if <variable>==<prompt>
# if (==) kondisi : aksi

# if (basic)
nama = input("masukan nama anda : ")
if nama=="hanif" : print("selamat datang pak Hanif")
print(f"silahkan masuk pak {nama}")

# if (indentation)
nama = input("masukan nama anda : ")
if nama=="hanif" : 
    print("selamat datang pak Hanif")
    print("CEO & Founder dari Several Oracles")
print(f"silahkan masuk pak {nama}")

# if & else & elif (indentation)
# jika ada lebih dari satu pilihan percabangan maka wajib menggunakan elif <variable>==<prompt>
nama = input("masukan nama anda : ")
if nama=="hanif" :
    print("Selamat datang pak hanif")
    print("CEO & Founder dari Several Oracles")
elif nama=="fixera" :
    print("Selamat datang pak fixera")
    print("Co-Founder dari Several Oracles")
else :
    print(f"selamat datang {nama}")
    print("jangan lupa absen! kerja!")
print("terima kasih")
