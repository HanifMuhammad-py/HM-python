#  pseudocode

# 1. Baca masalah → Terjemahkan ke bahasa manusia dulu
# Sebelum nulis kode, tulis di komentar apa yang mau dilakukan step by step dalam bahasa Indonesia.
# python
# 
# 1. Minta input nama dari user
# 2. Simpan ke dalam list
# 3. Tampilkan semua nama yang sudah masuk
# 4. Hitung berapa jumlahnya
# 
# Baru setelah itu isi kodenya. Ini namanya pseudocode, dan ini yang dilakukan programmer senior sebelum nulis satu baris pun.

# ----------------------------------------------------------------------------------------------------------

# 2. Pola "Data → Proses → Tampilkan"
# Hampir semua program sederhana punya struktur ini:
# INPUT → SIMPAN → PROSES → OUTPUT
# Contoh konkret:
# python# INPUT
# nama = input("Masukkan nama: ")

# # SIMPAN
# daftar_nama = []
# daftar_nama.append(nama)

# # PROSES
# jumlah = len(daftar_nama)

# # OUTPUT
# print(f"Total nama: {jumlah}")
# Kalau bingung mulai dari mana, tanya ke diri sendiri: "Datanya dari mana? Mau disimpan dimana? Mau diapakan? Mau ditampilkan bagaimana?"

# ----------------------------------------------------------------------------------------------------------

# 3. Pilih fungsi dengan pertanyaan ini
# Pertanyaan                                        jawabannya pakai
# -----------------------------------------------------------------------
# Perlu menyimpan banyak data?                      List / Dictionary
# Perlu ulangi sesuatu?                             For / While loop
# Perlu cek kondisi?                                If / elif / else
# Perlu reuse kode yang sama?                       def (function)
# Perlu simpan pasangan key-value?                  Dictionary

# ----------------------------------------------------------------------------------------------------------

# 4. Debug dengan cara baca dari atas ke bawah
# Kalau kode tidak jalan, baca seperti kamu adalah Python-nya. Tanya: "Di baris ini, variabel X isinya apa?" Tambahkan print() sementara di setiap langkah untuk cek nilainya.

# Saran latihan konkret buat kamu sekarang
# Karena kamu sudah punya semua file itu, coba buat 1 program gabungan per hari dengan tema sederhana. Misalnya:

# Program input data barang warung (pakai dictionary + loop + function)
# Kalkulator sederhana (pakai function + if/else + input)

# # Mulai dari pseudocode dulu, baru kode.
