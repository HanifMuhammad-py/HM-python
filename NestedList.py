print("Nested List")

# List Biasa
data_1 = ["hanif", "raja", "python"]
data_2 = ["several", "Oracles"]
data_3 = ["SAAS", "Automation", "Solution"]

# List 2D
# bisa membuat list, di dalam list dengan jenis data yang berbeda
data_x = [data_2, data_3, 13, 12]
print(data_x)

# Nested List
# for in

Peserta_1 = ["Hanif", 23, "Jakarta"]
Peserta_2 = ["Nipeh", 30, "Tangerang"]
Peserta_3 = ["Jokowi", 60, "Solo"]

list_peserta = [Peserta_1, Peserta_2, Peserta_3]
for peserta in list_peserta :
    print(f'"Nama\t\t: "{Peserta_1[0]}')
    print(f'"Umur\t\t: "{Peserta_1[1]}')
    print(f'"Domisili\t: "{Peserta_1[2]}\n')