print("Book List Project\n")

list_buku = []
while True :
    judul_buku = input("Masukan judul buku = ")
    penulis_buku = input("Masukan penulis buku = ")
    
    data = [judul_buku, penulis_buku]
    print(data)

    list_buku.append(data)
    print(list_buku)

    print("No.  |   Judul buku  |   Penulis Buku")
    for index, buku in enumerate (list_buku) :
        print(f'{index+1}   |,  {buku[0]} |, {buku[1]}')
        
        lanjut = input("apakah ingin lanjut ? (y/n)")
        if lanjut == "n": 
            break
        pass